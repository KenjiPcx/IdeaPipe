import React, { HTMLAttributes }from 'react';

interface ButtonProps extends HTMLAttributes<HTMLButtonElement> {
  size?: 'sm' | 'md' | 'lg';
}

export const Button: React.FC<ButtonProps> = ({ children, size = 'md', ...props }) => {
  const sizeClasses = {
    sm: 'px-2 py-1 text-sm',
    md: 'px-4 py-2',
    lg: 'px-6 py-3 text-lg',
  };

  return (
    <button
      className={`bg-blue-500 text-white font-bold rounded ${sizeClasses[size]}`}
      {...props}
    >
      {children}
    </button>
  );
};
