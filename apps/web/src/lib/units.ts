export const FEET_PER_METER = 3.28084;

export function metersToFeet(m: number): number {
  return m * FEET_PER_METER;
}