'use client';

import React from 'react';
import { useState } from 'react';
import { mockProblems } from '@/data/mockProblems';
import ProblemGrid from '@/components/ProblemGrid';
import FilterSidebar from '@/components/FilterSidebar';

const ProblemsPage: React.FC = () => {
  const [filteredProblems, setFilteredProblems] = useState(mockProblems);

  const categories = Array.from(new Set(mockProblems.map(p => p.category)));
  const difficulties = ['Easy', 'Medium', 'Hard'];

  const handleFilterChange = (filters: { categories: string[], difficulties: string[] }) => {
    const filtered = mockProblems.filter(problem => 
      (filters.categories.length === 0 || filters.categories.includes(problem.category)) &&
      (filters.difficulties.length === 0 || filters.difficulties.includes(problem.difficulty))
    );
    setFilteredProblems(filtered);
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <h1 className="text-3xl font-bold mb-8">Explore Problems</h1>
      <div className="flex">
        <FilterSidebar 
          categories={categories} 
          difficulties={difficulties} 
          onFilterChange={handleFilterChange} 
        />
        <div className="ml-8 flex-grow">
          <ProblemGrid problems={filteredProblems} />
        </div>
      </div>
    </div>
  );
}

export default ProblemsPage;
