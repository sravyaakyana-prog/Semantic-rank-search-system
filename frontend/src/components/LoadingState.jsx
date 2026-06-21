export default function LoadingState({ loadingText }) {
    return (
      <div className="max-w-5xl mx-auto mb-10">
        <div className="bg-slate-900 border border-cyan-500/30 rounded-3xl p-8">
  
          <div className="flex items-center gap-4">
            <div className="w-4 h-4 rounded-full bg-cyan-400 animate-pulse"></div>
            <span className="text-cyan-400 text-lg font-semibold">
              {loadingText}
            </span>
          </div>
  
          <div className="mt-5 h-2 bg-slate-800 rounded-full overflow-hidden">
            <div className="h-full bg-gradient-to-r from-cyan-400 to-purple-500 animate-pulse" />
          </div>
  
        </div>
      </div>
    );
  }