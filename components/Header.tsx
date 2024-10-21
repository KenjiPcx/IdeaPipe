import React from 'react';
import Link from 'next/link';
import { Button } from "./ui/button";

export default function Header() {
  return (
    <header className="border-b">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          <Link href="/" className="font-bold text-xl">
            IdeaGen
          </Link>
          <nav>
            <ul className="flex space-x-4">
              <li>
                <Link href="/problems">
                  <Button variant="ghost">Problems</Button>
                </Link>
              </li>
              <li>
                <Button>Submit Problem</Button>
              </li>
            </ul>
          </nav>
        </div>
      </div>
    </header>
  );
}
