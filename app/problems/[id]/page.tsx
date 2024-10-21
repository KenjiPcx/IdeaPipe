'use client';

import { useParams } from 'next/navigation';
import { mockProblems } from '@/data/mockProblems';

export default function ProblemPage() {
  const params = useParams();
  const id = params.id as string;
  const problem = mockProblems.find(p => p.id === id);

  if (!problem) {
    return <div>Problem not found</div>;
  }

  return (
    <div className="max-w-4xl mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold mb-4">{problem.title}</h1>
      <div className="flex gap-2 mb-4">
        <span className="bg-blue-100 text-blue-800 px-2 py-1 rounded-full text-sm">
          {problem.category}
        </span>
        <span className={`px-2 py-1 rounded-full text-sm ${
          problem.difficulty === 'Easy' ? 'bg-green-100 text-green-800' :
          problem.difficulty === 'Medium' ? 'bg-yellow-100 text-yellow-800' :
          'bg-red-100 text-red-800'
        }`}>
          {problem.difficulty}
        </span>
      </div>
      <p className="text-gray-700 mb-8">{problem.description}</p>
      <div className="bg-gray-50 p-4 rounded-lg">
        <h2 className="text-xl font-semibold mb-4">Proposed Solutions</h2>
        <p className="text-gray-600 italic">No solutions proposed yet. Be the first to suggest one!</p>
        {/* Add a form or button here to allow users to propose solutions */}
      </div>
    </div>
  );
}
