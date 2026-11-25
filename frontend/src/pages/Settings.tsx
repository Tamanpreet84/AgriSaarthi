import { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { useAppSettings, type Language } from '../context/AppSettingsContext';
import { User, Bell, Palette, Globe, Info, LogOut, Settings as SettingsIcon, Sun, Moon } from 'lucide-react';

export default function Settings() {
  const { user, logout } = useAuth();
  const { language, setLanguage, theme, toggleTheme, t } = useAppSettings();
  const navigate = useNavigate();

  const [notificationsEnabled, setNotificationsEnabled] = useState(() => {
    const saved = localStorage.getItem('agrisaarthi_notifications');
    return saved !== 'disabled';
  });

  const toggleNotifications = () => {
    const newVal = !notificationsEnabled;
    setNotificationsEnabled(newVal);
    localStorage.setItem('agrisaarthi_notifications', newVal ? 'enabled' : 'disabled');
  };

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  const languages: { code: Language; label: string; native: string }[] = [
    { code: 'en', label: 'English', native: 'EN' },
    { code: 'hi', label: 'Hindi', native: 'हिंदी' },
    { code: 'pa', label: 'Punjabi', native: 'ਪੰਜਾਬੀ' }
  ];

  return (
    <div className="max-w-3xl mx-auto space-y-6 md:space-y-8 pb-12">
      <div className="pt-4">
        <h1 className="text-2xl font-black text-slate-800 tracking-tight flex items-center">
          <SettingsIcon className="w-6 h-6 text-[#27ae60] mr-2" />
          {t('nav_settings')}
        </h1>
        <p className="text-sm text-slate-500 font-medium mt-1">Manage your preferences and application settings</p>
      </div>

      <div className="space-y-6">
        {/* Account Section */}
        <div className="bg-white rounded-2xl border border-slate-100 shadow-sm overflow-hidden">
          <div className="px-6 py-4 border-b border-slate-100 flex items-center bg-slate-50/50">
            <User className="w-5 h-5 text-[#27ae60] mr-2" />
            <h2 className="text-lg font-bold text-slate-800">Account</h2>
          </div>
          <div className="p-6">
            <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
              <div>
                <p className="text-sm font-semibold text-slate-800">{user?.fullName || 'Taman Preet Singh'}</p>
                <p className="text-sm text-slate-500">{user?.email || 'tamanpreet0007@gmail.com'}</p>
              </div>
              <Link
                to="/profile"
                className="inline-flex items-center justify-center px-4 py-2 border border-[#27ae60] text-[#27ae60] font-semibold rounded-lg hover:bg-[#27ae60] hover:text-white transition-colors text-sm"
              >
                View Profile
              </Link>
            </div>
          </div>
        </div>

        {/* Appearance & Language Section */}
        <div className="bg-white rounded-2xl border border-slate-100 shadow-sm overflow-hidden">
          <div className="px-6 py-4 border-b border-slate-100 flex items-center bg-slate-50/50">
            <Palette className="w-5 h-5 text-[#27ae60] mr-2" />
            <h2 className="text-lg font-bold text-slate-800">Appearance & Language</h2>
          </div>
          <div className="p-6 space-y-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm font-semibold text-slate-800">Color Theme</p>
                <p className="text-sm text-slate-500">Switch between crisp Light Mode and night-friendly Dark Mode.</p>
              </div>
              <button
                type="button"
                onClick={toggleTheme}
                className="inline-flex items-center space-x-2 px-4 py-2 rounded-xl border border-slate-200 bg-slate-50 hover:bg-emerald-50 text-slate-800 font-bold text-sm transition-colors cursor-pointer"
              >
                {theme === 'dark' ? (
                  <>
                    <Sun size={16} className="text-amber-400" />
                    <span>Light Mode</span>
                  </>
                ) : (
                  <>
                    <Moon size={16} className="text-amber-500" />
                    <span>Dark Mode</span>
                  </>
                )}
              </button>
            </div>

            <div className="pt-4 border-t border-slate-100 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
              <div className="flex items-start space-x-2">
                <Globe className="w-4 h-4 text-[#27ae60] mt-0.5 shrink-0" />
                <div>
                  <p className="text-sm font-semibold text-slate-800">Interface Language</p>
                  <p className="text-sm text-slate-500">Choose English, Hindi (हिंदी), or Punjabi (ਪੰਜਾਬੀ).</p>
                </div>
              </div>
              <div className="flex items-center bg-slate-100 rounded-xl p-1 border border-slate-200 self-start sm:self-auto">
                {languages.map((item) => (
                  <button
                    key={item.code}
                    type="button"
                    onClick={() => setLanguage(item.code)}
                    className={`px-3 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer ${
                      language === item.code
                        ? 'bg-white text-[#145a32] shadow-sm'
                        : 'text-slate-600 hover:text-[#145a32]'
                    }`}
                  >
                    {item.native}
                  </button>
                ))}
              </div>
            </div>
          </div>
        </div>

        {/* Notifications Section */}
        <div className="bg-white rounded-2xl border border-slate-100 shadow-sm overflow-hidden">
          <div className="px-6 py-4 border-b border-slate-100 flex items-center bg-slate-50/50">
            <Bell className="w-5 h-5 text-[#27ae60] mr-2" />
            <h2 className="text-lg font-bold text-slate-800">Notifications</h2>
          </div>
          <div className="p-6 flex items-center justify-between">
            <div className="pr-4">
              <p className="text-sm font-semibold text-slate-800">In-App Alerts</p>
              <p className="text-sm text-slate-500">Enable local alerts for weather and disease intelligence.</p>
            </div>
            <button
              type="button"
              onClick={toggleNotifications}
              className={`relative inline-flex h-6 w-11 shrink-0 cursor-pointer rounded-full border-2 border-transparent transition-colors duration-200 ease-in-out focus:outline-none focus:ring-2 focus:ring-[#27ae60] focus:ring-offset-2 ${
                notificationsEnabled ? 'bg-[#27ae60]' : 'bg-slate-300'
              }`}
            >
              <span
                className={`pointer-events-none inline-block h-5 w-5 transform rounded-full bg-white shadow ring-0 transition duration-200 ease-in-out ${
                  notificationsEnabled ? 'translate-x-5' : 'translate-x-0'
                }`}
              />
            </button>
          </div>
        </div>

        {/* Application Info Section */}
        <div className="bg-white rounded-2xl border border-slate-100 shadow-sm overflow-hidden">
          <div className="px-6 py-4 border-b border-slate-100 flex items-center bg-slate-50/50">
            <Info className="w-5 h-5 text-[#27ae60] mr-2" />
            <h2 className="text-lg font-bold text-slate-800">Application Information</h2>
          </div>
          <div className="p-6 space-y-2">
            <h3 className="text-lg font-black text-[#145a32]">AgriSaarthi</h3>
            <p className="text-sm font-semibold text-slate-800">AI-Powered Crop Advisory & Farmer’s Companion</p>
            <p className="text-sm text-[#27ae60] font-bold tracking-wide">KNOW MORE GROW MORE</p>
            <p className="text-xs text-slate-500 mt-4">Version: 1.0</p>
          </div>
        </div>

        {/* Logout Section */}
        <div className="bg-white rounded-2xl border border-red-100 shadow-sm overflow-hidden mt-8">
          <div className="p-6 flex flex-col md:flex-row md:items-center justify-between gap-4">
            <div>
              <p className="text-sm font-bold text-red-600">Sign Out</p>
              <p className="text-sm text-slate-500">Log out of your current session on this device.</p>
            </div>
            <button
              type="button"
              onClick={handleLogout}
              className="inline-flex items-center justify-center px-4 py-2 bg-red-50 text-red-600 font-semibold rounded-lg hover:bg-red-100 transition-colors text-sm cursor-pointer"
            >
              <LogOut className="w-4 h-4 mr-2" />
              {t('logout')}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
