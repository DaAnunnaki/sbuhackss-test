const RESET_KEY = "reminders_last_reset";

export function shouldResetNow(now = Date.now()): boolean {
  const last = Number(localStorage.getItem(RESET_KEY) || 0);
  return now - last >= 24 * 60 * 60 * 1000;
}
export function markResetNow(now = Date.now()) {
  localStorage.setItem(RESET_KEY, String(now));
}
