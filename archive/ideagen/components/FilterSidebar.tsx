import { useState } from 'react';

interface FilterSidebarProps {
  categories: string[];
  difficulties: string[];
  onFilterChange: (filters: { categories: string[], difficulties: string[] }) => void;
}

export default function FilterSidebar({ categories, difficulties, onFilterChange }: FilterSidebarProps) {
  const [selectedCategories, setSelectedCategories] = useState<string[]>([]);
  const [selectedDifficulties, setSelectedDifficulties] = useState<string[]>([]);

  const handleCategoryChange = (category: string) => {
    const updatedCategories = selectedCategories.includes(category)
      ? selectedCategories.filter(c => c !== category)
      : [...selectedCategories, category];
    setSelectedCategories(updatedCategories);
    onFilterChange({ categories: updatedCategories, difficulties: selectedDifficulties });
  };

  const handleDifficultyChange = (difficulty: string) => {
    const updatedDifficulties = selectedDifficulties.includes(difficulty)
      ? selectedDifficulties.filter(d => d !== difficulty)
      : [...selectedDifficulties, difficulty];
    setSelectedDifficulties(updatedDifficulties);
    onFilterChange({ categories: selectedCategories, difficulties: updatedDifficulties });
  };

  return (
    <div className="w-64 bg-white shadow-md rounded-lg p-6">
      <h2 className="text-xl font-semibold mb-4">Filters</h2>
      
      <div className="mb-6">
        <h3 className="font-medium mb-2">Categories</h3>
        {categories.map(category => (
          <div key={category} className="flex items-center mb-2">
            <input
              type="checkbox"
              id={`category-${category}`}
              checked={selectedCategories.includes(category)}
              onChange={() => handleCategoryChange(category)}
              className="mr-2"
            />
            <label htmlFor={`category-${category}`}>{category}</label>
          </div>
        ))}
      </div>

      <div>
        <h3 className="font-medium mb-2">Difficulty</h3>
        {difficulties.map(difficulty => (
          <div key={difficulty} className="flex items-center mb-2">
            <input
              type="checkbox"
              id={`difficulty-${difficulty}`}
              checked={selectedDifficulties.includes(difficulty)}
              onChange={() => handleDifficultyChange(difficulty)}
              className="mr-2"
            />
            <label htmlFor={`difficulty-${difficulty}`}>{difficulty}</label>
          </div>
        ))}
      </div>
    </div>
  );
}
