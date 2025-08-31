"use client";
import { useEffect } from "react";
import AOS from "aos";

export default function AOSInit() {
  useEffect(() => {
    AOS.init({ duration: 600, easing: "ease-out-quart", once: true });
  }, []);
  return null;
}
