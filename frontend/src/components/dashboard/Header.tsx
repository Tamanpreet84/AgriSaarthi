import { useState, useRef, useEffect } from 'react';
import { Bell, LogOut, Menu, Sun, Moon, CheckCheck, AlertTriangle, TrendingUp, CloudSun } from 'lucide-react';
import { useAuth } from '../../context/AuthContext';
import { useAppSettings, type Language } from '../../context/AppSettingsContext';
import { useNavigate, Link } from 'react-router-dom';

interface HeaderProps {
  onMenuClick?: () => void;
}

export default function Header({ onMenuClick }: HeaderProps) {
  const { user, logout } = useAuth();
  const { language, setLanguage, theme, toggleTheme, t } = useAppSettings();
  const navigate = useNavigate();

  const [notifOpen, setNotifOpen] = useState(false);
  const [unreadCount, setUnreadCount] = useState(3);
  const notifRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (notifRef.current && !notifRef.current.contains(event.target as Node)) {
        setNotifOpen(false);
      }
    };
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  const getInitials = (name: string) => {
    return name
      .split(' ')
      .map(n => n[0])
      .join('')
      .toUpperCase()
      .substring(0, 2);
  };

  const initials = user?.fullName ? getInitials(user.fullName) : 'TP';

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  const alerts = [
    {
      id: 1,
      title: 'Yellow Rust Sentry Alert',
      desc: 'Inspect wheat leaf undersides in Doaba & Kapurthala belt.',
      time: '2 hrs ago',
      to: '/pest-disease',
      icon: <AlertTriangle size={16} className="text-amber-600" />,
      bg: 'bg-amber-50'
    },
    {
      id: 2,
      title: 'Mandi Price Gain: Wheat & Paddy',
      desc: 'Khanna & Amritsar Mandi modal rates updated.',
      time: '5 hrs ago',
      to: '/market-prices',
      icon: <TrendingUp size={16} className="text-emerald-600" />,
      bg: 'bg-emerald-50'
    },
    {
      id: 3,
      title: 'Favorable Spray Window',
      desc: 'Calm winds (11.2 km/h) expected for next 48 hours.',
      time: '1 day ago',
      to: '/weather',
      icon: <CloudSun size={16} className="text-sky-600" />,
      bg: 'bg-sky-50'
    }
  ];

  const languages: { code: Language; label: string }[] = [
    { code: 'en', label: 'EN' },
    { code: 'hi', label: 'हिंदी' },
    { code: 'pa', label: 'ਪੰਜਾਬੀ' }
  ];

  return (
    <div className="bg-[#f3f7f5] lg:bg-transparent px-4 md:px-6 lg:px-8 py-3.5 flex items-center justify-between gap-3 border-b border-slate-200/60 lg:border-b-0">
      {/* Left: Mobile Drawer Trigger */}
      <div className="flex items-center space-x-3">
        <button
          type="button"
          onClick={onMenuClick}
          className="lg:hidden p-2 text-slate-600 hover:text-[#145a32] bg-white rounded-xl border border-slate-200 shadow-sm transition-colors"
          aria-label="Open Navigation Menu"
        >
          <Menu size={20} />
        </button>
        <div className="hidden sm:flex items-center space-x-2 bg-white/80 backdrop-blur-sm px-3 py-1.5 rounded-full border border-emerald-100 shadow-xs">
          <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
          <span className="text-[11px] font-bold text-[#145a32] tracking-wide">AgriSaarthi Live Platform</span>
        </div>
      </div>

      {/* Right Actions */}
      <div className="flex items-center justify-end space-x-2 sm:space-x-3 shrink-0">
        {/* Theme Toggle Button */}
        <button
          type="button"
          onClick={toggleTheme}
          title={theme === 'dark' ? 'Switch to Light Mode' : 'Switch to Dark Mode'}
          className="flex items-center space-x-1.5 px-3 py-1.5 rounded-xl border border-slate-200 bg-white hover:bg-slate-50 text-slate-700 text-xs font-bold shadow-xs transition-all cursor-pointer"
        >
          {theme === 'dark' ? (
            <>
              <Sun size={15} className="text-amber-400" />
              <span className="hidden sm:inline">Light</span>
            </>
          ) : (
            <>
              <Moon size={15} className="text-amber-500" />
              <span className="hidden sm:inline">Dark</span>
            </>
          )}
        </button>

        {/* Multilingual Language Switcher */}
        <div className="flex items-center bg-slate-100 rounded-xl p-1 text-xs font-bold border border-slate-200">
          {languages.map((item) => (
            <button
              key={item.code}
              type="button"
              onClick={() => setLanguage(item.code)}
              className={`px-2 sm:px-2.5 py-1 rounded-lg transition-all cursor-pointer ${
                language === item.code
                  ? 'bg-white text-[#145a32] shadow-xs font-extrabold'
                  : 'text-slate-600 hover:text-[#145a32]'
              }`}
            >
              {item.label}
            </button>
          ))}
        </div>

        {/* Notifications Bell Dropdown */}
        <div className="relative" ref={notifRef}>
          <button
            type="button"
            onClick={() => setNotifOpen(!notifOpen)}
            aria-label="Notifications"
            className="relative p-2 text-slate-600 bg-white hover:bg-emerald-50 hover:text-[#145a32] border border-slate-200 rounded-full shadow-xs transition-all cursor-pointer"
          >
            <Bell size={18} />
            {unreadCount > 0 && (
              <span className="absolute -top-0.5 -right-0.5 w-4 h-4 bg-red-500 text-white text-[9px] font-bold rounded-full flex items-center justify-center border-2 border-white">
                {unreadCount}
              </span>
            )}
          </button>

          {notifOpen && (
            <div className="absolute right-0 mt-2 w-80 bg-white rounded-2xl shadow-xl border border-slate-200 z-50 overflow-hidden">
              <div className="px-4 py-3 border-b border-slate-100 flex items-center justify-between bg-slate-50">
                <h4 className="text-xs font-bold text-slate-800 uppercase tracking-wider">{t('notifications_title')}</h4>
                <button
                  type="button"
                  onClick={() => setUnreadCount(0)}
                  className="text-[11px] font-semibold text-[#27ae60] hover:underline flex items-center gap-1 cursor-pointer"
                >
                  <CheckCheck size={13} />
                  {t('mark_read')}
                </button>
              </div>
              <div className="divide-y divide-slate-100 max-h-72 overflow-y-auto">
                {alerts.map((alert) => (
                  <button
                    key={alert.id}
                    type="button"
                    onClick={() => {
                      setNotifOpen(false);
                      setUnreadCount(0);
                      navigate(alert.to);
                    }}
                    className="w-full text-left px-4 py-3 hover:bg-slate-50 transition-colors flex items-start space-x-3 cursor-pointer"
                  >
                    <div className={`w-8 h-8 rounded-lg ${alert.bg} flex items-center justify-center shrink-0 mt-0.5`}>
                      {alert.icon}
                    </div>
                    <div className="flex-1 min-w-0">
                      <div className="flex justify-between items-center">
                        <p className="text-xs font-bold text-slate-800 truncate">{alert.title}</p>
                        <span className="text-[10px] text-slate-400 shrink-0 ml-2">{alert.time}</span>
                      </div>
                      <p className="text-[11px] text-slate-500 mt-0.5 leading-snug">{alert.desc}</p>
                    </div>
                  </button>
                ))}
              </div>
            </div>
          )}
        </div>

        {/* Clickable Profile Pill */}
        <Link
          to="/profile"
          title={t('nav_profile')}
          className="flex items-center space-x-2.5 p-1 pr-2 rounded-full bg-white hover:bg-emerald-50 border border-slate-200 shadow-xs transition-all"
        >
          <div className="w-8 h-8 rounded-full bg-[#e8f3ee] flex items-center justify-center border border-[#27ae60]/30 text-[#145a32] font-bold text-xs">
            {initials}
          </div>
          <div className="hidden md:block text-left">
            <p className="text-xs font-bold text-slate-800 leading-tight max-w-[110px] truncate">{user?.fullName || 'Taman Preet'}</p>
            <p className="text-[10px] text-slate-500 font-medium">{t('farmer_role')}</p>
          </div>
        </Link>

        {/* Logout Button */}
        <button
          type="button"
          onClick={handleLogout}
          className="p-2 text-slate-500 hover:text-red-600 bg-white hover:bg-red-50 border border-slate-200 rounded-full shadow-xs transition-colors cursor-pointer"
          title={t('logout')}
        >
          <LogOut size={18} />
        </button>
      </div>
    </div>
  );
}
