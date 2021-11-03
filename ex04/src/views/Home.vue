<template>
  <div class="inputoutput">
    <img id="imageSrc" alt="No Image" v-on:load="onLoadImage" />
    <div class="caption">imageSrc <input v-on:change='handleChange'
      type="file" id="fileInput" name="file" /></div>
  </div>
  <div class="inputoutput">
    <canvas id="canvasOutput" ></canvas>
    <div class="caption">canvasOutput
      <button v-on:click="handleRotate">Rotate</button>
      <button v-on:click="handleSave">Save</button>
    </div>
  </div>
</template>

<script>
import cv from '@/assets/opencv';

export default {
  data() {
    return {

    };
  },
  methods: {
    handleChange(e) {
      const imgElement = document.getElementById('imageSrc');
      imgElement.src = URL.createObjectURL(e.target.files[0]);
    },
    onLoadImage() {
      const imgElement = document.getElementById('imageSrc');
      const mat = cv.imread(imgElement);
      cv.imshow('canvasOutput', mat);
    },
    handleRotate() {
      const mat = cv.imread('canvasOutput');
      cv.rotate(mat, mat, cv.ROTATE_90_CLOCKWISE);
      cv.imshow('canvasOutput', mat);
    },
    handleSave() {
      const link = document.createElement('a');
      const canvas = document.getElementById('canvasOutput');
      link.download = 'download.png';
      link.href = canvas.toDataURL();
      link.click();
      link.delete();
    },
  },
};
</script>

<style>

</style>
