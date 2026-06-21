export default function SearchBar({ query, setQuery, onSearch, loading }) {
    return (
      <div className="flex gap-4 mb-16 max-w-5xl mx-auto">
        <input
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Search documents, concepts, topics..."
          className="flex-1 bg-slate-900/80 border border-slate-700 rounded-2xl p-5 text-lg outline-none focus:border-cyan-400"
        />
  
        <button
          onClick={onSearch}
          disabled={loading}
          className="px-10 rounded-2xl bg-cyan-500 hover:bg-cyan-400 text-black font-bold transition disabled:opacity-50"
        >
          Search
        </button>
      </div>
    );
  }