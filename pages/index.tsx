import React, { useState } from 'react';
import { Problem } from '../types/Problem';
import ProblemList from '../components/ProblemList';
import ProblemForm from '../components/ProblemForm';
import axios from 'axios';

const Home = (): JSX.Element => {
  const [problems, setProblems] = useState<Problem[]>([]);
  const [selectedProblem, setSelectedProblem] = useState<Problem | null>(null);
  const [matches, setMatches] = useState<string>('');
  const [loading, setLoading] = useState<boolean>(false);

  const handleProblemSelect = async (problem: Problem) => {
    setSelectedProblem(problem);
    setLoading(true);
    try {
      const response = await axios.post('/api/match', { problem_id: problem.id });
      setMatches(response.data.matches);
    } catch (error) {
      console.error('Error matching problem:', error);
      setMatches('An error occurred while matching the problem.');
    }
    setLoading(false);
  };

  const handleProblemSubmit = (problem: Problem) => {
    setProblems([...problems, problem]);
  };

  return (
    <div className="container mx-auto px-4">
      <h1 className="text-3xl font-bold mb-4">Problem-Solution Matcher</h1>
      <div className="grid grid-cols-2 gap-4">
        <div>
          <ProblemList problems={problems} onProblemSelect={handleProblemSelect} />
          <ProblemForm onSubmit={handleProblemSubmit} />
        </div>
        <div>
          {selectedProblem && (
            <div className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
              <h2 className="text-xl font-bold mb-2">Selected Problem: {selectedProblem.title}</h2>
              <p className="mb-4">{selectedProblem.content}</p>
              {loading ? (
                <p>Matching solutions...</p>
              ) : (
                matches && (
                  <div>
                    <h3 className="text-lg font-bold mb-2">Matched Solutions:</h3>
                    <pre className="bg-gray-100 p-4 rounded">{matches}</pre>
                  </div>
                )
              )}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default Home;
