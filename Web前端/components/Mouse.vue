<template>x:{{ x }} y:{{ y }} sourceType:{{ sourceType }}</template>

<script setup>
import { useMouse } from "@vueuse/core";
const { x = 0, y = 0, sourceType} = useMouse();
</script>