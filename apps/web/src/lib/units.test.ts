import { describe, expect, it } from "vitest";
import { metersToFeet } from "@/lib/units";

describe("metersToFeet", () => {
  it("converts Mount Rainier's summit height", () => {
    expect(metersToFeet(4392)).toBeCloseTo(14409.5, 0);
  });

  it("maps zero to zero", () => {
    expect(metersToFeet(0)).toBe(0);
  });
});