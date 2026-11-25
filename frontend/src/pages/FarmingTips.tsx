import { API_BASE_URL, fetchWithTimeout } from '../config';
import { useState, useEffect, useMemo } from 'react';
import { useAuth } from '../context/AuthContext';
import { Lightbulb, Search, Loader2, Filter, ChevronDown, ChevronUp } from 'lucide-react';

interface FarmingTip {
  id: string;
  category: string;
  crop: string;
  title: string;
  description: string;
  actionableAdvice: string;
}

const FALLBACK_TIPS: FarmingTip[] = [
  {
    id: 'ft_1',
    category: 'Soil preparation',
    crop: 'All',
    title: 'Deep Ploughing',
    description: 'Perform deep summer ploughing to expose soil-borne pathogens and pests to intense heat.',
    actionableAdvice: 'Plough fields up to 15-20cm deep during May-June before the onset of monsoons.'
  },
  {
    id: 'ft_2',
    category: 'Irrigation',
    crop: 'Rice',
    title: 'Alternate Wetting and Drying',
    description: 'AWD is a water-saving technology that farmers can apply to reduce their irrigation water consumption.',
    actionableAdvice: 'Let the field dry out for 1-3 days after the ponded water drops to 15cm below the soil surface before re-flooding.'
  },
  {
    id: 'ft_3',
    category: 'Sustainable farming',
    crop: 'All',
    title: 'Green Manuring',
    description: 'Incorporate green manure crops like Dhaincha or Sunhemp before transplanting the main crop to enrich soil nitrogen.',
    actionableAdvice: 'Sow green manure crop seeds 45 days before the main crop and plough them back into the soil at the flowering stage.'
  },
  {
    id: 'ft_4',
    category: 'Disease prevention',
    crop: 'Tomato',
    title: 'Staking and Pruning',
    description: 'Keeping leaves off the soil reduces early blight and soil-borne infections.',
    actionableAdvice: 'Tie tomato plants to wooden stakes or trellises 3-4 weeks after transplanting. Prune the bottom 12 inches of leaves.'
  },
  {
    id: 'ft_5',
    category: 'Pest monitoring',
    crop: 'Cotton',
    title: 'Pheromone Traps',
    description: 'Pheromone traps monitor the adult moth population of Pink Bollworm.',
    actionableAdvice: 'Install 5 traps per hectare exactly at crop canopy level starting 45 days after sowing.'
  },
  {
    id: 'ft_6',
    category: 'Water conservation',
    crop: 'Wheat',
    title: 'Zero Tillage',
    description: 'Planting wheat without tilling the soil preserves moisture, reduces cost, and prevents weed emergence.',
    actionableAdvice: 'Use a Zero Till Seed-cum-Fertilizer Drill to sow seeds directly into the residue of the previous crop.'
  },
  {
    id: 'ft_7',
    category: 'Crop rotation',
    crop: 'Potato',
    title: 'Legume Rotation',
    description: 'Rotating potatoes with legumes breaks the cycle of soil-borne diseases like common scab and late blight.',
    actionableAdvice: 'Avoid planting potatoes in the same field for more than 1 year in a 3-year cycle. Rotate with beans or peas.'
  },
  {
    id: 'ft_8',
    category: 'Organic matter/compost',
    crop: 'Sugarcane',
    title: 'Trash Mulching',
    description: 'Leaving sugarcane trash as mulch conserves moisture, suppresses weeds, and adds organic matter to the soil over time.',
    actionableAdvice: 'Spread dried sugarcane leaves between rows instead of burning them after harvest.'
  }
];

export default function FarmingTips() {
  const { token } = useAuth();
  const [allTips, setAllTips] = useState<FarmingTip[]>(FALLBACK_TIPS);
  const [loading, setLoading] = useState(false);

  const [searchCategory, setSearchCategory] = useState('');
  const [searchCrop, setSearchCrop] = useState('');
  const [expandedId, setExpandedId] = useState<string | null>('ft_1');

  useEffect(() => {
    const fetchTips = async () => {
      try {
        const res = await fetchWithTimeout(`${API_BASE_URL}/api/farming-tips`, {
          headers: { 'Authorization': `Bearer ${token}` }
        }, 2000);
        if (res.ok) {
          const data = await res.json();
          if (Array.isArray(data) && data.length > 0) {
            setAllTips(data);
          }
        }
      } catch {
        // Verified fallback already active
      } finally {
        setLoading(false);
      }
    };
    fetchTips();
  }, [token]);

  const tips = useMemo(() => {
    return allTips.filter(t => {
      const matchCat =
        !searchCategory ||
        t.category.toLowerCase().includes(searchCategory.toLowerCase()) ||
        t.title.toLowerCase().includes(searchCategory.toLowerCase());
      const matchCrop = !searchCrop || t.crop.toLowerCase().includes(searchCrop.toLowerCase());
      return matchCat && matchCrop;
    });
  }, [allTips, searchCategory, searchCrop]);

  return (
    <div className="flex-1 bg-slate-50 min-h-screen pb-12">
      <header className="bg-white border-b border-slate-200 px-6 py-5 sticky top-0 z-10 flex flex-col sm:flex-row sm:items-center justify-between gap-4 rounded-t-2xl">
        <div>
          <h1 className="text-2xl font-black text-slate-800 tracking-tight flex items-center">
            <Lightbulb className="w-6 h-6 text-amber-500 mr-2" />
            Farming Tips
          </h1>
          <p className="text-sm text-slate-500 font-medium mt-1">Actionable agricultural guidance</p>
        </div>
      </header>

      <div className="max-w-4xl mx-auto px-4 sm:px-6 py-8 space-y-6">
        <div className="bg-white p-4 rounded-xl shadow-sm border border-slate-200 flex flex-col sm:flex-row gap-4">
          <div className="relative flex-1">
            <Filter className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400 w-4 h-4" />
            <input
              type="text"
              placeholder="Filter by category (e.g., Irrigation)..."
              value={searchCategory}
              onChange={(e) => setSearchCategory(e.target.value)}
              className="w-full pl-9 pr-4 py-2 bg-slate-50 border border-slate-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-amber-500/20 focus:border-amber-500"
            />
          </div>
          <div className="relative flex-1">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400 w-4 h-4" />
            <input
              type="text"
              placeholder="Filter by crop (e.g., Wheat, Rice)..."
              value={searchCrop}
              onChange={(e) => setSearchCrop(e.target.value)}
              className="w-full pl-9 pr-4 py-2 bg-slate-50 border border-slate-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-amber-500/20 focus:border-amber-500"
            />
          </div>
          {(searchCategory || searchCrop) && (
            <button
              type="button"
              onClick={() => { setSearchCategory(''); setSearchCrop(''); }}
              className="px-4 py-2 bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-bold rounded-lg transition-colors cursor-pointer"
            >
              Clear
            </button>
          )}
        </div>

        {loading ? (
          <div className="flex flex-col items-center justify-center py-12">
            <Loader2 className="w-8 h-8 text-amber-500 animate-spin mb-4" />
            <p className="text-slate-500 font-medium">Loading farming tips...</p>
          </div>
        ) : tips.length === 0 ? (
          <div className="bg-white rounded-xl p-12 text-center border border-slate-200 shadow-sm">
            <Lightbulb className="w-12 h-12 text-slate-300 mx-auto mb-4" />
            <h3 className="text-lg font-bold text-slate-700 mb-1">No tips found</h3>
            <p className="text-slate-500 text-sm mb-4">Try adjusting your filters.</p>
            <button
              type="button"
              onClick={() => { setSearchCategory(''); setSearchCrop(''); }}
              className="px-4 py-2 bg-[#145a32] text-white text-xs font-bold rounded-lg cursor-pointer"
            >
              Show All Tips
            </button>
          </div>
        ) : (
          <div className="space-y-4">
            {tips.map((t) => {
              const isExpanded = expandedId === t.id;
              return (
                <div key={t.id} className="bg-white rounded-xl border border-slate-200 shadow-sm overflow-hidden transition-all">
                  <button
                    type="button"
                    className="w-full text-left p-5 flex items-center justify-between cursor-pointer hover:bg-slate-50"
                    onClick={() => setExpandedId(isExpanded ? null : t.id)}
                  >
                    <div className="pr-4">
                      <div className="flex items-center space-x-2 mb-1.5">
                        <span className="text-[10px] font-bold uppercase tracking-wider text-amber-600 bg-amber-50 px-2 py-0.5 rounded">{t.category}</span>
                        <span className="text-[10px] font-bold uppercase tracking-wider text-slate-500 bg-slate-100 px-2 py-0.5 rounded">{t.crop}</span>
                      </div>
                      <h3 className="text-base font-bold text-slate-800">{t.title}</h3>
                    </div>
                    {isExpanded ? <ChevronUp className="w-5 h-5 text-slate-400 shrink-0" /> : <ChevronDown className="w-5 h-5 text-slate-400 shrink-0" />}
                  </button>

                  {isExpanded && (
                    <div className="px-5 pb-5 pt-2 border-t border-slate-100 bg-slate-50/50">
                      <p className="text-sm text-slate-600 mb-4 leading-relaxed">{t.description}</p>
                      <div className="bg-emerald-50 border border-emerald-100 rounded-lg p-3">
                        <h4 className="text-xs font-bold text-emerald-800 dark:text-emerald-300 mb-1">Actionable Advice:</h4>
                        <p className="text-sm text-emerald-700 dark:text-emerald-400">{t.actionableAdvice}</p>
                      </div>
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        )}
      </div>
    </div>
  );
}
