import { Problem } from '@/data/mockProblems';
import ProblemCard from './ProblemCard';

interface ProblemGridProps {
  problems: Problem[];
}

export default function ProblemGrid({ problems }: ProblemGridProps) {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      {problems.map((problem) => (
        <ProblemCard key={problem.id} problem={problem} />
      ))}
    </div>
  );
}
