import './assets/index.css'
import Contents from './templates/Contents.svelte'
import Header from "./templates/Header.svelte";
import Loader from "./templates/Loader.svelte";

// const loader = new Loader({
//   target: document.getElementById('loader'),
// })

const header = new Header({
  target: document.getElementById('header'),
})

const contents = new Contents({
  target: document.getElementById('contents'),
})

export default [header, contents]
