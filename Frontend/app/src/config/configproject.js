const PRODUCTION = true;

let URL_BACKEND;
let API_KEY_THEMOVIEDB = "eac810b6ade616ce25d01396797173f0";

if(PRODUCTION === false) {
    URL_BACKEND = "http://127.0.0.1:8000/moviereview/";    
}
else{
    URL_BACKEND = "https://apimoviereview.herokuapp.com/moviereview/";
}

let config = {
    URL_BACKEND,
    API_KEY_THEMOVIEDB
}; 

export default config;
