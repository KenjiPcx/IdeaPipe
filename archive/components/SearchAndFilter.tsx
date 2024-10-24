import React, { useState } from 'react';

interface SearchAndFilterProps {
  onSearch: (query: string) => void;
  onFilterChange: (category: string, difficulty: string) => void;
}

const SearchAndFilter: React.FC<SearchAndFilterProps> = ({ onSearch, onFilterChange }) => {
  const [searchQuery, setSearchQuery] = useState('');
  const [category, setCategory] = useState('');
  const [difficulty, setDifficulty] = useState('');

  const handleSearch = () => {
    onSearch(searchQuery);
  };

  const handleFilterChange = () => {
    onFilterChange(category, difficulty);
  };

  return (
    <div className="mb-4">
      <input
        type="text"
        value={searchQuery}
        onChange={(e) => setSearchQuery(e.target.value)}
        placeholder="Search problems"
        className="border p-2 mr-2"
      />
      <select
        value={category}
        onChange={(e) => setCategory(e.target.value)}
        className="border p-2 mr-2"
      >
        <option value="">All Categories</option>
        {/* Add category options */}
      </select>
      <select
        value={difficulty}
        onChange={(e) => setDifficulty(e.target.value)}
        className="border p-2 mr-2"
      >
        <option value="">All Difficulties</option>
        {/* Add difficulty options */}
      </select>
      <button onClick={handleSearch} className="bg-blue-500 text-white px-4 py-2 rounded">
        Search
      </button>
      <button onClick={handleFilterChange} className="bg-gray-300 px-4 py-2 rounded ml-2">
        Apply Filters
      </button>
    </div>
  );
};

export default SearchAndFilter;
