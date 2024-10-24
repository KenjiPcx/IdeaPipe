import { mockProblems } from '@/data/mockProblems';
import { notFound } from 'next/navigation';

export default function ProblemPage({ params }: { params: { id: string } }) {
  const problem = mockProblems.find(p => p.id === params.id);

  if (!problem) {
    notFound();
  }

  return (
    <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <h1 className="text-3xl font-bold mb-4">{problem.title}</h1>
      <p className="text-gray-600 mb-6">{problem.description}</p>
      <div className="flex items-center space-x-4 mb-8">
        <span className="text-sm font-medium text-blue-600">{problem.category}</span>
        <span className={`text-sm font-medium px-2 py-1 rounded-full ${
          problem.difficulty === 'Easy' ? 'bg-green-100 text-green-800' :
          problem.difficulty === 'Medium' ? 'bg-yellow-100 text-yellow-800' :
          'bg-red-100 text-red-800'
        }`}>
          {problem.difficulty}
        </span>
      </div>
      {/* Add more problem details and interaction elements here */}
    </div>
  );
}
