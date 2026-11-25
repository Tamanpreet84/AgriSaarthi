import { API_BASE_URL } from '../config';
import { useState, useEffect } from 'react';
import { ShieldAlert, Bug, Activity } from 'lucide-react';
import { useAuth } from '../context/AuthContext';

const FALLBACK_CROPS = [
  { id: 'wheat', name: 'Wheat (Triticum aestivum)' },
  { id: 'rice', name: 'Rice (Oryza sativa)' },
  { id: 'tomato', name: 'Tomato (Solanum lycopersicum)' },
  { id: 'potato', name: 'Potato (Solanum tuberosum)' },
  { id: 'cotton', name: 'Cotton (Gossypium)' },
  { id: 'pepper_bell', name: 'Pepper / Bell Pepper' }
];

const FALLBACK_DISEASES: Record<string, any[]> = {
  wheat: [
    {
      name: 'Wheat Yellow Rust (Stripe Rust)',
      severity: 'High',
      symptoms: ['Yellow to orange pustules in linear stripes on upper leaf surfaces', 'Reduced grain filling and premature leaf senescence'],
      favorableConditions: ['Cool temperatures (10-18°C)', 'High morning dew and humid foggy conditions'],
      prevention: ['Grow rust-resistant varieties like HD 3086 or PBW 826', 'Avoid excessive nitrogen top-dressing'],
      management: ['Spray Propiconazole 25% EC (Tilt) @ 1 ml/L water', 'Apply Tebuconazole 250 EC upon early stripe appearance']
    }
  ],
  rice: [
    {
      name: 'Rice Blast (Magnaporthe oryzae)',
      severity: 'High',
      symptoms: ['Diamond-shaped spindle lesions with gray centers on leaves', 'Neck rot breaking panicles at base'],
      favorableConditions: ['Long dew periods and cloudy humid weather', 'High nitrogen application'],
      prevention: ['Use certified disease-free seed with Tricyclazole seed treatment', 'Maintain split balanced nitrogen'],
      management: ['Spray Tricyclazole 75% WP @ 0.6 g/L water', 'Avoid standing water stagnation during heading']
    }
  ],
  tomato: [
    {
      name: 'Tomato Early Blight (Alternaria solani)',
      severity: 'Moderate',
      symptoms: ['Concentric dark target-board rings on older lower leaves', 'Yellowing halo around necrotic spots'],
      favorableConditions: ['Warm temperatures (24-29°C)', 'Alternating wet and dry spells'],
      prevention: ['Staking and pruning lower leaves off soil', 'Drip irrigation instead of overhead sprinklers'],
      management: ['Spray Mancozeb 75% WP @ 2.5 g/L', 'Apply Azoxystrobin or copper fungicide at 10-day intervals']
    }
  ],
  potato: [
    {
      name: 'Potato Late Blight (Phytophthora infestans)',
      severity: 'High',
      symptoms: ['Water-soaked dark patches expanding across leaf margins', 'White cottony fungal growth beneath leaves in humidity'],
      favorableConditions: ['Humidity > 85% and cool temperatures (12-22°C)', 'Cloudy misty weather'],
      prevention: ['Earthing up soil cleanly around ridges', 'Use blight-tolerant seed tubers'],
      management: ['Apply Cymoxanil + Mancozeb @ 2.5 g/L', 'Destroy infected haulms before tuber harvest']
    }
  ],
  cotton: [
    {
      name: 'Cotton Bacterial Blight (Angular Leaf Spot)',
      severity: 'Moderate',
      symptoms: ['Angular water-soaked lesions restricted by leaf veins', 'Black arm streaks along petioles and stems'],
      favorableConditions: ['Warm humid winds (28-35°C) with monsoon splashes'],
      prevention: ['Acid-delinted certified seeds', 'Crop rotation with non-malvaceous crops'],
      management: ['Spray Copper Oxychloride 50% WP @ 2.5 g/L + Streptocycline', 'Avoid excess field water']
    }
  ],
  pepper_bell: [
    {
      name: 'Pepper Bacterial Spot',
      severity: 'High',
      symptoms: ['Small yellow-green water-soaked spots turning brown/black', 'Raised scab-like spots on fruit'],
      favorableConditions: ['Warm weather (24-30°C)', 'Frequent rain or overhead irrigation'],
      prevention: ['Use disease-free transplants and rotate crops'],
      management: ['Apply copper-based bactericides early in the season', 'Remove infected crop debris']
    }
  ]
};

const FALLBACK_PESTS: Record<string, any[]> = {
  wheat: [
    {
      name: 'Wheat Aphids',
      severity: 'Moderate',
      symptoms: ['Clusters of pale green aphids sucking sap from earheads and flag leaves', 'Honeydew secretion causing sooty mold'],
      favorableConditions: ['Warm dry spells during February–March grain filling'],
      prevention: ['Encourage natural ladybird beetles along field bunds'],
      management: ['Spray Imidacloprid 17.8% SL @ 0.5 ml/L only if threshold exceeds 10 aphids/earhead']
    }
  ],
  rice: [
    {
      name: 'Brown Planthopper (BPH)',
      severity: 'High',
      symptoms: ['Circular patches of drying plants known as hopper burn', 'Basal stem crowding just above water line'],
      favorableConditions: ['Dense spacing, excessive nitrogen, and continuous standing water'],
      prevention: ['Leave 30 cm alleyways every 2 meters', 'Drain field periodically'],
      management: ['Spray Pymetrozine 50% WG or Dinotefuran directed at plant base']
    }
  ],
  tomato: [
    {
      name: 'Tomato Hornworm',
      severity: 'High',
      symptoms: ['Large green caterpillars causing rapid leaf defoliation', 'Dark droppings on foliage'],
      favorableConditions: ['Warm summer temperatures and solanaceous weeds'],
      prevention: ['Deep summer ploughing and weed-free borders'],
      management: ['Handpick larvae on small plots', 'Use Bacillus thuringiensis (Bt) bio-spray']
    }
  ],
  potato: [
    {
      name: 'Potato Aphids (Myzus persicae)',
      severity: 'Moderate',
      symptoms: ['Curled stunted young leaves and sticky honeydew', 'Vector for Potato Leaf Roll Virus'],
      favorableConditions: ['Warm dry weather and excess urea'],
      prevention: ['Use yellow sticky traps and balanced NPK'],
      management: ['Spray Neem oil 1500 ppm or Thiamethoxam 25 WG']
    }
  ],
  cotton: [
    {
      name: 'Pink Bollworm',
      severity: 'High',
      symptoms: ['Rosette flowers and damaged lint inside bolls', 'Exit holes in green bolls'],
      favorableConditions: ['Warm humid post-monsoon flowering stage'],
      prevention: ['Install 5 pheromone traps per hectare at canopy height', 'Timely crop termination'],
      management: ['Neem seed kernel extract (NSKE 5%) early', 'Recommended selective bollworm spray at ETL']
    }
  ],
  pepper_bell: [
    {
      name: 'Whitefly (Bemisia tabaci)',
      severity: 'Moderate',
      symptoms: ['Clouds of tiny white moths when leaves are touched', 'Leaf yellowing and curl virus spread'],
      favorableConditions: ['Warm dry greenhouse or open-field summer weather'],
      prevention: ['Yellow sticky cards and weed-free field margins'],
      management: ['Neem oil formulation or horticultural insecticidal soap']
    }
  ]
};

export default function PestDisease() {
  const { token } = useAuth();
  const [crops, setCrops] = useState<any[]>(FALLBACK_CROPS);
  const [selectedCrop, setSelectedCrop] = useState<string>('wheat');
  const [diseases, setDiseases] = useState<any[]>(FALLBACK_DISEASES.wheat);
  const [pests, setPests] = useState<any[]>(FALLBACK_PESTS.wheat);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetchCrops();
  }, [token]);

  useEffect(() => {
    if (selectedCrop) {
      fetchKnowledge(selectedCrop);
    }
  }, [selectedCrop, token]);

  const fetchCrops = async () => {
    try {
      const res = await fetch(`${API_BASE_URL}/api/agri-knowledge/crops`, {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      if (res.ok) {
        const data = await res.json();
        if (Array.isArray(data) && data.length > 0) {
          setCrops(data);
          if (!selectedCrop) setSelectedCrop(data[0].id);
        }
      }
    } catch {
      // Fallback already populated
    }
  };

  const fetchKnowledge = async (cropId: string) => {
    setLoading(true);
    try {
      const [dRes, pRes] = await Promise.all([
        fetch(`${API_BASE_URL}/api/agri-knowledge/diseases?crop=${cropId}`, {
          headers: { 'Authorization': `Bearer ${token}` }
        }),
        fetch(`${API_BASE_URL}/api/agri-knowledge/pests?crop=${cropId}`, {
          headers: { 'Authorization': `Bearer ${token}` }
        })
      ]);

      let gotDiseases: any[] = [];
      let gotPests: any[] = [];
      if (dRes.ok) gotDiseases = await dRes.json();
      if (pRes.ok) gotPests = await pRes.json();

      setDiseases(gotDiseases.length > 0 ? gotDiseases : (FALLBACK_DISEASES[cropId] || []));
      setPests(gotPests.length > 0 ? gotPests : (FALLBACK_PESTS[cropId] || []));
      setLoading(false);
      return;
    } catch {
      // Resilient fallback
    }

    setDiseases(FALLBACK_DISEASES[cropId] || FALLBACK_DISEASES.wheat);
    setPests(FALLBACK_PESTS[cropId] || FALLBACK_PESTS.wheat);
    setLoading(false);
  };

  return (
    <div className="max-w-6xl mx-auto space-y-6">
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
        <div>
          <h1 className="text-2xl font-bold text-slate-800 flex items-center gap-2">
            <ShieldAlert className="w-8 h-8 text-[#27ae60]" />
            Pest & Disease Intelligence
          </h1>
          <p className="text-slate-500">Explore comprehensive knowledge about crop risks, prevention, and management.</p>
        </div>

        <div className="w-full md:w-64">
          <label className="block text-sm font-medium text-slate-700 mb-1">Select Crop</label>
          <select
            value={selectedCrop}
            onChange={(e) => setSelectedCrop(e.target.value)}
            className="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-[#27ae60] focus:border-transparent outline-none bg-white cursor-pointer"
          >
            {crops.map(c => (
              <option key={c.id} value={c.id}>{c.name}</option>
            ))}
          </select>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Diseases Section */}
        <div className="space-y-4">
          <h2 className="text-xl font-bold text-slate-800 flex items-center gap-2 border-b pb-2">
            <Activity className="w-5 h-5 text-red-500" />
            Common Diseases
          </h2>
          {loading ? (
            <p className="text-slate-400 text-sm">Loading disease profiles...</p>
          ) : diseases.length === 0 ? (
            <p className="text-slate-500 italic">No major diseases cataloged for this crop.</p>
          ) : (
            diseases.map((d, i) => <KnowledgeCard key={i} data={d} type="Disease" />)
          )}
        </div>

        {/* Pests Section */}
        <div className="space-y-4">
          <h2 className="text-xl font-bold text-slate-800 flex items-center gap-2 border-b pb-2">
            <Bug className="w-5 h-5 text-orange-500" />
            Common Pests
          </h2>
          {loading ? (
            <p className="text-slate-400 text-sm">Loading pest profiles...</p>
          ) : pests.length === 0 ? (
            <p className="text-slate-500 italic">No major pests cataloged for this crop.</p>
          ) : (
            pests.map((p, i) => <KnowledgeCard key={i} data={p} type="Pest" />)
          )}
        </div>
      </div>
    </div>
  );
}

function KnowledgeCard({ data, type }: { data: any, type: string }) {
  if (data.severity === 'None') return null;

  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden">
      <div className="p-4 bg-slate-50 border-b border-slate-100 flex justify-between items-start">
        <div>
          <h3 className="font-bold text-slate-800 text-lg">{data.name}</h3>
          <span className={`text-xs font-semibold px-2 py-1 rounded-full mt-1 inline-block ${
            data.severity === 'High' ? 'bg-red-100 text-red-700' : 'bg-orange-100 text-orange-700'
          }`}>
            {type} • {data.severity} Severity
          </span>
        </div>
      </div>
      <div className="p-4 space-y-4 text-sm">
        {data.symptoms && data.symptoms.length > 0 && (
          <div>
            <h4 className="font-semibold text-slate-800 mb-1">Symptoms</h4>
            <ul className="list-disc pl-5 text-slate-600 space-y-1">
              {data.symptoms.map((s: string, i: number) => <li key={i}>{s}</li>)}
            </ul>
          </div>
        )}

        {data.favorableConditions && data.favorableConditions.length > 0 && (
          <div>
            <h4 className="font-semibold text-slate-800 mb-1">Favorable Conditions</h4>
            <ul className="list-disc pl-5 text-slate-600 space-y-1">
              {data.favorableConditions.map((s: string, i: number) => <li key={i}>{s}</li>)}
            </ul>
          </div>
        )}

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-2">
          {data.prevention && data.prevention.length > 0 && (
            <div className="bg-green-50 p-3 rounded-lg border border-green-100">
              <h4 className="font-semibold text-green-800 mb-1">Prevention</h4>
              <ul className="list-disc pl-4 text-green-700 space-y-1 text-xs">
                {data.prevention.map((s: string, i: number) => <li key={i}>{s}</li>)}
              </ul>
            </div>
          )}

          {data.management && data.management.length > 0 && (
            <div className="bg-blue-50 p-3 rounded-lg border border-blue-100">
              <h4 className="font-semibold text-blue-800 mb-1">Management</h4>
              <ul className="list-disc pl-4 text-blue-700 space-y-1 text-xs">
                {data.management.map((s: string, i: number) => <li key={i}>{s}</li>)}
              </ul>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
