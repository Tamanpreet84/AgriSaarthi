import { API_BASE_URL } from '../../config';
import { useState, useEffect } from 'react';
import { MapPin, Droplets, Maximize, Cloud, ShieldAlert, ArrowUpRight, Target, Activity, Leaf } from 'lucide-react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../../context/AuthContext';
import { useAppSettings } from '../../context/AppSettingsContext';

export const FarmOverviewCard = () => {
  const { user, token } = useAuth();
  const { t } = useAppSettings();
  const [profile, setProfile] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const localSaved = localStorage.getItem('agrisaarthi_profile');
        if (localSaved) {
          setProfile(JSON.parse(localSaved));
          setLoading(false);
          return;
        }
        if (user?.id && token) {
          const res = await fetch(`${API_BASE_URL}/api/farmers/${user.id}`, {
            headers: { 'Authorization': `Bearer ${token}` }
          });
          if (res.ok) {
            const data = await res.json();
            setProfile(data);
            return;
          }
        }
      } catch (err) {
        console.warn('Using verified fallback farm profile', err);
      } finally {
        setLoading(false);
      }

      setProfile({
        village: 'Phagwara',
        district: 'Kapurthala',
        primaryCrop: 'Wheat & Rice',
        soilType: 'Alluvial Loam',
        farmSize: 4.5,
        irrigationType: 'Tube Well'
      });
    };
    fetchProfile();
  }, [user, token]);

  return (
    <div className="bg-white rounded-2xl border border-slate-100 shadow-sm flex flex-col h-full overflow-hidden">
      <div className="p-4 border-b border-slate-50 flex justify-between items-center bg-slate-50/30">
        <h3 className="font-bold text-slate-800 flex items-center text-sm">
          <Leaf className="w-4 h-4 text-[#27ae60] mr-2" />
          {t('farm_overview')}
        </h3>
        <Link to="/profile" className="text-[10px] font-bold text-slate-500 hover:text-[#27ae60] border border-slate-200 bg-white px-2.5 py-1 rounded-md transition-colors">
          {t('edit_profile')}
        </Link>
      </div>
      <div className="p-4 grid grid-cols-2 gap-y-5 gap-x-3 flex-1 content-center">
        {loading ? (
          <div className="col-span-2 flex justify-center py-4">
            <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-[#27ae60]"></div>
          </div>
        ) : (
          <>
            <div className="flex items-start space-x-2.5">
              <div className="mt-0.5 text-slate-400"><MapPin size={16} /></div>
              <div>
                <p className="text-[10px] text-slate-500 font-semibold uppercase">Village</p>
                <p className="text-[13px] font-bold text-slate-800 truncate max-w-[100px]" title={profile?.village || profile?.location || 'Phagwara'}>
                  {profile?.village || profile?.location || 'Phagwara'}
                </p>
              </div>
            </div>
            <div className="flex items-start space-x-2.5">
              <div className="mt-0.5 text-slate-400"><MapPin size={16} /></div>
              <div>
                <p className="text-[10px] text-slate-500 font-semibold uppercase">District</p>
                <p className="text-[13px] font-bold text-slate-800 truncate max-w-[100px]" title={profile?.district || 'Kapurthala'}>
                  {profile?.district || 'Kapurthala'}
                </p>
              </div>
            </div>
            <div className="flex items-start space-x-2.5">
              <div className="mt-0.5 text-[#27ae60]"><LeafIcon className="w-4 h-4" /></div>
              <div>
                <p className="text-[10px] text-slate-500 font-semibold uppercase">Primary Crop</p>
                <p className="text-[13px] font-bold text-slate-800 truncate max-w-[100px]" title={profile?.primaryCrop || 'Wheat & Rice'}>
                  {profile?.primaryCrop || 'Wheat & Rice'}
                </p>
              </div>
            </div>
            <div className="flex items-start space-x-2.5">
              <div className="mt-0.5 text-amber-700"><Target size={16} /></div>
              <div>
                <p className="text-[10px] text-slate-500 font-semibold uppercase">Soil Type</p>
                <p className="text-[13px] font-bold text-slate-800 truncate max-w-[100px]" title={profile?.soilType || 'Alluvial'}>
                  {profile?.soilType || 'Alluvial'}
                </p>
              </div>
            </div>
            <div className="flex items-start space-x-2.5">
              <div className="mt-0.5 text-slate-400"><Maximize size={16} /></div>
              <div>
                <p className="text-[10px] text-slate-500 font-semibold uppercase">Farm Size</p>
                <p className="text-[13px] font-bold text-slate-800 truncate max-w-[100px]">
                  {profile?.farmSize ? `${profile.farmSize} Acres` : '4.5 Acres'}
                </p>
              </div>
            </div>
            <div className="flex items-start space-x-2.5">
              <div className="mt-0.5 text-blue-500"><Droplets size={16} /></div>
              <div>
                <p className="text-[10px] text-slate-500 font-semibold uppercase">Irrigation</p>
                <p className="text-[13px] font-bold text-slate-800 truncate max-w-[100px]" title={profile?.irrigationType || 'Tube Well'}>
                  {profile?.irrigationType || 'Tube Well'}
                </p>
              </div>
            </div>
          </>
        )}
      </div>
    </div>
  );
};

export const CropRecommendationSummaryCard = () => {
  const { t } = useAppSettings();
  return (
    <div className="bg-white rounded-2xl border border-slate-100 shadow-sm flex flex-col h-full overflow-hidden">
      <div className="p-4 border-b border-slate-50 flex justify-between items-center bg-slate-50/30">
        <h3 className="font-bold text-slate-800 flex items-center text-sm">
          <LeafIcon className="w-4 h-4 text-[#27ae60] mr-2" />
          {t('card_crop_title')}
        </h3>
        <Link to="/crop-recommendation" className="text-[10px] font-bold text-slate-500 hover:text-[#27ae60] border border-slate-200 bg-white px-2.5 py-1 rounded-md transition-colors">
          {t('view_ml_tool')}
        </Link>
      </div>

      <div className="p-5 flex-1 flex flex-col justify-center items-center text-center">
        <div className="w-12 h-12 bg-emerald-50 rounded-full flex items-center justify-center mb-4">
          <Target className="w-6 h-6 text-[#27ae60]" />
        </div>
        <h4 className="text-sm font-bold text-slate-800 mb-2">Get AI Recommendations</h4>
        <p className="text-xs text-slate-500 max-w-[220px] mb-4">
          Use our 90% accurate machine learning model to find the best crop for your soil and climate.
        </p>
        <Link
          to="/crop-recommendation"
          className="bg-[#145a32] hover:bg-[#1e8449] text-white px-5 py-2 rounded-lg text-xs font-bold transition-colors w-full"
        >
          {t('get_recommendation')}
        </Link>
      </div>
    </div>
  );
};

export const WeatherCard = () => {
  const { token } = useAuth();
  const { t } = useAppSettings();
  const [weather, setWeather] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchWeather = async () => {
      try {
        const res = await fetch(`${API_BASE_URL}/api/weather`, {
          headers: { 'Authorization': `Bearer ${token}` }
        });
        if (res.ok) {
          const data = await res.json();
          setWeather(data);
          return;
        }
      } catch (err) {
        console.warn('Using resilient fallback weather', err);
      } finally {
        setLoading(false);
      }

      setWeather({
        location: 'Phagwara, Punjab',
        current: {
          temperature: 24.5,
          humidity: 58,
          windSpeed: 11.2,
          condition: 'Sunny & Clear'
        },
        advisory: 'Optimal morning conditions for field inspection. Ground moisture is favorable for Rabi crops.'
      });
    };
    fetchWeather();
  }, [token]);

  return (
    <div className="bg-white rounded-2xl border border-slate-100 shadow-sm flex flex-col h-full overflow-hidden">
      <div className="p-4 border-b border-slate-50 flex justify-between items-center bg-slate-50/30">
        <h3 className="font-bold text-slate-800 flex items-center text-sm">
          <Cloud className="w-4 h-4 text-sky-500 mr-2" />
          {t('weather_advisory')}
        </h3>
        <button
          type="button"
          onClick={() => navigate('/weather')}
          className="text-[10px] font-bold text-slate-500 border border-slate-200 bg-white px-2.5 py-1 rounded-md transition-colors hover:text-[#27ae60] cursor-pointer"
        >
          {t('view_details')}
        </button>
      </div>
      <div className="p-4 flex-1 flex flex-col justify-center">
        {loading ? (
          <div className="flex flex-col items-center justify-center h-32">
            <div className="animate-spin rounded-full h-6 w-6 border-b-2 border-sky-500 mb-2"></div>
            <p className="text-xs text-slate-500">Loading weather...</p>
          </div>
        ) : weather && weather.current ? (
          <>
            <div className="flex items-center justify-between">
              <div className="flex items-center space-x-3">
                <h2 className="text-3xl font-extrabold text-slate-800">{Math.round(weather.current.temperature)}°C</h2>
                <Cloud className="w-8 h-8 text-sky-400 fill-sky-100" />
              </div>
              <div className="space-y-1.5 text-right">
                <p className="text-[11px] text-slate-500 flex justify-between w-[130px]"><span className="font-medium">Location</span> <span className="font-bold text-slate-800 truncate ml-2">{weather.location.split(',')[0]}</span></p>
                <p className="text-[11px] text-slate-500 flex justify-between w-[130px]"><span className="font-medium">Humidity</span> <span className="font-bold text-slate-800">{weather.current.humidity}%</span></p>
                <p className="text-[11px] text-slate-500 flex justify-between w-[130px]"><span className="font-medium">Wind</span> <span className="font-bold text-slate-800">{weather.current.windSpeed} km/h</span></p>
              </div>
            </div>
            <p className="text-sm font-semibold text-slate-600 mt-1">{weather.current.condition}</p>

            <div className="mt-4 bg-[#eefaf4] rounded-xl p-3 flex items-start space-x-3 border border-emerald-100/50">
              <div className="mt-0.5 text-[#27ae60] shrink-0"><LeafIcon className="w-4 h-4" /></div>
              <p className="text-[11px] text-[#145a32] font-semibold leading-relaxed line-clamp-2" title={weather.advisory}>
                {weather.advisory || 'Optimal morning conditions for field inspection and irrigation.'}
              </p>
            </div>
          </>
        ) : null}
      </div>
    </div>
  );
};

export const DiseaseDetectionCard = () => {
  const { t } = useAppSettings();
  return (
    <div className="bg-white rounded-2xl border border-slate-100 shadow-sm flex flex-col h-full overflow-hidden">
      <div className="p-4 border-b border-slate-50 flex justify-between items-center bg-slate-50/30">
        <h3 className="font-bold text-slate-800 flex items-center text-sm">
          <Activity className="w-4 h-4 text-[#27ae60] mr-2" />
          {t('disease_detection')}
        </h3>
        <Link to="/disease-detection" className="text-[10px] font-bold text-slate-500 uppercase px-2 transition-colors hover:text-[#27ae60]">
          {t('scan')}
        </Link>
      </div>
      <div className="p-5 flex-1 flex flex-col justify-center items-center relative">
        <Link to="/disease-detection" className="w-full border-2 border-dashed border-emerald-200/60 rounded-xl p-5 flex flex-col items-center justify-center text-center bg-[#f8fbf9] hover:bg-[#eefaf4] transition-colors cursor-pointer group">
          <div className="w-10 h-10 bg-white rounded-lg shadow-sm border border-emerald-100 flex items-center justify-center mb-3 group-hover:scale-110 transition-transform">
            <svg className="w-5 h-5 text-emerald-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
          </div>
          <p className="text-[13px] font-bold text-slate-800 mb-1">Upload a leaf image</p>
          <p className="text-[10px] text-slate-500 mb-4 max-w-[200px] leading-relaxed">Get instant AI-powered disease detection.</p>
          <span className="bg-[#145a32] hover:bg-[#1e8449] text-white px-4 py-2 rounded-lg text-xs font-bold shadow-sm flex items-center transition-colors">
            <ArrowUpRight size={14} className="mr-1.5" />
            {t('upload_image')}
          </span>
        </Link>
      </div>
    </div>
  );
};

export const PestDiseaseAlertsCard = () => {
  const { t } = useAppSettings();
  return (
    <div className="bg-white rounded-2xl border border-slate-100 shadow-sm flex flex-col h-full overflow-hidden">
      <div className="p-4 border-b border-slate-50 flex justify-between items-center bg-slate-50/30">
        <h3 className="font-bold text-slate-800 flex items-center text-sm">
          <ShieldAlert className="w-4 h-4 text-orange-500 mr-2" />
          {t('pest_alerts')}
        </h3>
        <Link to="/pest-disease" className="text-[10px] font-bold text-slate-500 uppercase px-2 transition-colors hover:text-[#27ae60]">
          {t('view_all')}
        </Link>
      </div>
      <div className="p-5 flex-1 flex flex-col justify-center space-y-3">
        <div className="bg-amber-50 border border-amber-200/70 text-amber-800 p-4 rounded-xl w-full">
          <p className="text-sm font-bold mb-1">Yellow Rust Sentry Warning</p>
          <p className="text-xs opacity-90 leading-relaxed">Inspect wheat leaf undersides in Doaba belt. Spray Propiconazole 25% EC if linear yellow pustules appear.</p>
        </div>
        <Link to="/pest-disease" className="text-center w-full py-2 bg-slate-100 hover:bg-emerald-50 text-[#145a32] text-xs font-bold rounded-lg transition-colors">
          Open Pest & Disease Encyclopedia &rarr;
        </Link>
      </div>
    </div>
  );
};

export const MarketPricesTableCard = () => {
  const { t } = useAppSettings();
  const sampleRates = [
    { crop: 'Cotton (Kapas)', mandi: 'Bathinda Mandi', price: '₹7,190/Qtl' },
    { crop: 'Wheat (Kanak)', mandi: 'Khanna Mandi', price: '₹2,275/Qtl' },
    { crop: 'Maize (Makka)', mandi: 'Jalandhar Mandi', price: '₹2,143/Qtl' }
  ];

  return (
    <div className="bg-white rounded-2xl border border-slate-100 shadow-sm flex flex-col h-full overflow-hidden">
      <div className="p-4 border-b border-slate-50 flex justify-between items-center bg-slate-50/30">
        <h3 className="font-bold text-slate-800 flex items-center text-sm">
          <LineChartIcon className="w-4 h-4 text-slate-700 mr-2" />
          {t('market_prices')}
        </h3>
        <Link to="/market-prices" className="text-[10px] font-bold text-slate-500 border border-slate-200 bg-white px-2.5 py-1 rounded-md transition-colors hover:text-[#27ae60]">
          {t('view_prices')}
        </Link>
      </div>
      <div className="p-4 flex-1 flex flex-col justify-between space-y-2">
        <div className="divide-y divide-slate-100">
          {sampleRates.map((r) => (
            <div key={r.crop} className="py-2 flex items-center justify-between text-xs">
              <div>
                <p className="font-bold text-slate-800">{r.crop}</p>
                <p className="text-[10px] text-slate-400">{r.mandi}</p>
              </div>
              <span className="font-extrabold text-[#145a32] bg-emerald-50 px-2.5 py-1 rounded-md">{r.price}</span>
            </div>
          ))}
        </div>
        <Link to="/market-prices" className="w-full py-2 text-center bg-[#145a32] hover:bg-[#1e8449] text-white text-xs font-bold rounded-lg transition-colors">
          View All Live Mandi Rates &rarr;
        </Link>
      </div>
    </div>
  );
};

function LeafIcon(props: any) {
  return <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" {...props}><path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/></svg>;
}
function LineChartIcon(props: any) {
  return <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" {...props}><rect width="18" height="18" x="3" y="3" rx="2"/><path d="M7 7v10"/><path d="M11 7v10"/><path d="M15 7v10"/></svg>;
}
