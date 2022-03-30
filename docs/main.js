mapboxgl.accessToken =
  "pk.eyJ1IjoiY2FyZGVybmUiLCJhIjoiY2puMXN5cnBtNG53NDN2bnhlZ3h4b3RqcCJ9.eNjrtezXwvM7Ho1VSxo06w";

const map = new mapboxgl.Map({
  container: "map",
  style: "mapbox://styles/carderne/cl1dib41b005n15nt2c5zwd3l?fresh=true",
  center: [-2.5, 53],
  zoom: 6.5,
});
