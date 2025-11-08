import { Dayjs } from "dayjs";

export type Lang = "en" | "zh" | "es";

export type CalendarEvent = {
  id: string;
  title: string;
  start: Dayjs; // inclusive
  end: Dayjs;   // exclusive
};

export type Task = { id: string; label: string; time: string; done: boolean };

// Hours shown in week view
export const HOURS_START = 6;   // 6 AM
export const HOURS_END = 22;    // 10 PM

export const hoursArray = (start = HOURS_START, end = HOURS_END) =>
  Array.from({ length: end - start + 1 }, (_, i) => start + i);

export const minutesFromDayStart = (d: Dayjs) => d.hour() * 60 + d.minute();
