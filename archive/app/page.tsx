import React from 'react';
import Link from 'next/link';
import { Button } from "@/components/ui/button";

export default function Home() {
  return (
    <div className="max-w-4xl mx-auto px-4 py-16 text-center">
      <h1 className="text-4xl font-bold mb-6">Welcome to IdeaGen</h1>
      <p className="text-xl mb-8">Discover and solve real-world problems. Find your next big idea or contribute to existing ones.</p>
      <Link href="/problems">
        <Button size="lg">Explore Problems</Button>
      </Link>
    </div>
  );
}
