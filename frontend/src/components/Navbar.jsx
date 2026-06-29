import { Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export default function Navbar() {
  const { user, logout } = useAuth();

  return (
    <nav className="flex justify-between items-center mb-16">
      <Link
        to="/"
        className="text-2xl font-bold bg-gradient-to-r from-cyan-400 to-purple-500 bg-clip-text text-transparent"
      >
        SemanticRank AI
      </Link>

      <div className="flex items-center gap-6">
        <div className="hidden md:flex gap-8 text-slate-400">
          <Link to="/" className="hover:text-white">
            Search
          </Link>

          <Link to="/evaluation" className="hover:text-white">
            Analytics
          </Link>

          <span className="hover:text-white cursor-pointer">
            Architecture
          </span>

          <span className="hover:text-white cursor-pointer">
            GitHub
          </span>
        </div>

        {user && (
          <div className="flex items-center gap-4">
            <div className="text-sm text-slate-300">
              👋 {user.name}
            </div>

            <button
              onClick={logout}
              className="px-4 py-2 rounded-xl bg-red-500/20 border border-red-500/30 text-red-300 hover:bg-red-500/30 transition"
            >
              Logout
            </button>
          </div>
        )}
      </div>
    </nav>
  );
}