import React from 'react';
import { useState } from 'react';

interface FilterSidebarProps {
  categories: string[];
  difficulties: string[];
  onFilterChange: (filters: { categories: string[], difficulties: string[] }) => void;
}

const FilterSidebar = ({ categories, difficulties, onFilterChange }: FilterSidebarProps) => {
  const [selectedCategories, setSelectedCategories] = useState([]);
  const [selectedDifficulties, setSelectedDifficulties] = useState([]);

  const handleCategoryChange = (category: string) => {
    setSelectedCategories(prev => 
      prev.includes(category) ? prev.filter(c => c !== category) : [...prev, category]
    );
  };

  const handleDifficultyChange = (difficulty: string) => {
    setSelectedDifficulties(prev => 
      prev.includes(difficulty) ? prev.filter(d => d !== difficulty) : [...prev, difficulty]
    );
  };

  const applyFilters = () => {
    onFilterChange({ categories: selectedCategories, difficulties: selectedDifficulties });
  };

  return (
    <div className="space-y-4">
      <h2 className="text-lg font-semibold">Filters</h2>
      <div>
        <h3 className="font-medium mb-2">Categories</h3>
        {categories.map((category) => (
          <label key={category} className="flex items-center space-x-2">
            <input
              type="checkbox"
              checked={selectedCategories.includes(category)}
              onChange={() => handleCategoryChange(category)}
            />
            <span>{category}</span>
          </label>
        ))}
      </div>
      <div>
        <h3 className="font-medium mb-2">Difficulty</h3>
        {difficulties.map((difficulty) => (
          <label key={difficulty} className="flex items-center space-x-2">
            <input
              type="checkbox"
              checked={selectedDifficulties.includes(difficulty)}
              onChange={() => handleDifficultyChange(difficulty)}
            />
            <span>{difficulty}</span>
          </label>
        ))}
      </div>
      <button
        onClick={applyFilters}
        className="w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-600"
      >
        Apply Filters
      </button>
    </div>
  );
};

export default FilterSidebar;
