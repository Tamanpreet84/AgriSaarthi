import { Link, useLocation, useNavigate } from 'react-router-dom';
import { useAuth } from '../../context/AuthContext';
import { useAppSettings } from '../../context/AppSettingsContext';
import { 
  Home, User, Leaf, ShieldAlert, CloudSun, Bug, 
  LineChart, Lightbulb, BookOpen, Settings, LogOut, X 
} from 'lucide-react';
import logoUrl from '../../assets/logo.jpg';

interface SidebarProps {
  isOpen?: boolean;
  onClose?: () => void;
}

export default function Sidebar({ isOpen = false, onClose }: SidebarProps) {
  const { logout } = useAuth();
  const { t } = useAppSettings();
  const navigate = useNavigate();
  const location = useLocation();

  const handleLogout = () => {
    onClose?.();
    logout();
    navigate('/login');
  };

  const navItems = [
    { name: t('nav_dashboard'), path: '/dashboard', icon: <Home size={18} /> },
    { name: t('nav_profile'), path: '/profile', icon: <User size={18} /> },
    { name: t('nav_crop'), path: '/crop-recommendation', icon: <Leaf size={18} /> },
    { name: t('nav_disease'), path: '/disease-detection', icon: <ShieldAlert size={18} /> },
    { name: t('nav_weather'), path: '/weather', icon: <CloudSun size={18} /> },
    { name: t('nav_pest'), path: '/pest-disease', icon: <Bug size={18} /> },
    { name: t('nav_market'), path: '/market-prices', icon: <LineChart size={18} /> },
    { name: t('nav_tips'), path: '/farming-tips', icon: <Lightbulb size={18} /> },
    { name: t('nav_knowledge'), path: '/knowledge-hub', icon: <BookOpen size={18} /> },
    { name: t('nav_settings'), path: '/settings', icon: <Settings size={18} /> },
  ];

  const renderContent = () => (
    <div className="h-full bg-white flex flex-col border-r border-slate-100 shadow-[2px_0_10px_rgba(0,0,0,0.02)]">
      {/* Logo */}
      <div className="p-5 flex items-center justify-between lg:justify-center border-b border-slate-50 relative">
        <Link to="/dashboard" onClick={() => onClose?.()} className="flex flex-col items-center">
          <div className="w-14 h-14 rounded-full bg-emerald-50 flex items-center justify-center mb-2 overflow-hidden border border-emerald-100 p-1">
            <img src={logoUrl} alt="AgriSaarthi Logo" className="w-full h-full object-contain rounded-full" />
          </div>
          <h1 className="text-xl font-bold text-[#145a32] tracking-tight">AgriSaarthi</h1>
          <p className="text-[9px] text-[#27ae60] uppercase tracking-wider font-semibold mt-0.5 text-center leading-tight max-w-[200px]">
            {t('brand_tag')}
          </p>
          <div className="h-[1px] w-8 bg-[#27ae60] mt-1.5 opacity-50"></div>
          <p className="text-[7px] text-slate-400 tracking-widest mt-1">{t('know_more')}</p>
        </Link>

        {onClose && (
          <button
            type="button"
            onClick={onClose}
            className="lg:hidden absolute top-4 right-4 p-1.5 text-slate-500 hover:text-slate-800 rounded-lg hover:bg-slate-100"
            aria-label="Close Menu"
          >
            <X size={20} />
          </button>
        )}
      </div>

      {/* Nav Links */}
      <div className="flex-1 overflow-y-auto py-4 px-3 custom-scrollbar">
        <ul className="space-y-1">
          {navItems.map((item) => {
            const isActive = location.pathname === item.path;
            return (
              <li key={item.path}>
                <Link
                  to={item.path}
                  onClick={() => onClose?.()}
                  className={`flex items-center px-4 py-2.5 rounded-lg transition-all duration-200 ${
                    isActive
                      ? 'bg-emerald-50 text-[#145a32] font-semibold'
                      : 'text-slate-600 hover:bg-slate-50 hover:text-[#27ae60]'
                  }`}
                >
                  <span className={`mr-3 ${isActive ? 'text-[#27ae60]' : 'text-slate-400'}`}>
                    {item.icon}
                  </span>
                  <span className="text-sm">{item.name}</span>
                </Link>
              </li>
            );
          })}
        </ul>
      </div>

      {/* Knowledge Hub Card */}
      <div className="p-4">
        <div className="bg-emerald-50 rounded-xl p-4 border border-emerald-100/50 relative overflow-hidden">
          <div className="absolute top-0 right-0 p-2 opacity-10">
            <BookOpen size={48} className="text-[#145a32]" />
          </div>
          <h4 className="font-bold text-[#145a32] text-sm relative z-10">{t('need_advice')}</h4>
          <p className="text-xs text-[#27ae60] mb-3 relative z-10">{t('explore_resources')}</p>
          <Link
            to="/knowledge-hub"
            onClick={() => onClose?.()}
            className="w-full bg-[#145a32] hover:bg-[#1e8449] text-white text-xs font-semibold py-2 px-3 rounded-lg transition-colors flex items-center justify-between relative z-10"
          >
            <span>{t('nav_knowledge')}</span>
            <span>&rarr;</span>
          </Link>
        </div>

        <button
          type="button"
          onClick={handleLogout}
          className="mt-4 flex items-center px-4 py-2 text-sm text-slate-500 hover:text-red-600 transition-colors w-full cursor-pointer"
        >
          <LogOut size={18} className="mr-3" />
          {t('logout')}
        </button>
      </div>
    </div>
  );

  return (
    <>
      {/* Desktop Static Sidebar */}
      <div className="hidden lg:block h-full">{renderContent()}</div>

      {/* Mobile Slide-Over Drawer */}
      {isOpen && (
        <div className="lg:hidden fixed inset-0 z-50 flex">
          <div
            className="fixed inset-0 bg-black/50 backdrop-blur-xs transition-opacity"
            onClick={() => onClose?.()}
          />
          <div className="relative w-72 max-w-[85vw] h-full z-50">
            {renderContent()}
          </div>
        </div>
      )}
    </>
  );
}
