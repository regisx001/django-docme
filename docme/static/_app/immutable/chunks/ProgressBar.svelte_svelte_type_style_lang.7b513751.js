import{w as o}from"./index.b9740d9d.js";import{a9 as w}from"./index.1da8e345.js";let L=o("API Docs | Skeleton UI"),C=o("introduction"),v=o("Introduction"),E=o("Introduction"),b=o({theme:"skeleton"});const i={};function h(e){return e==="local"?localStorage:sessionStorage}function m(e,r,t){const a=(t==null?void 0:t.serializer)??JSON,f=(t==null?void 0:t.storage)??"local";function u(c,l){h(f).setItem(c,a.stringify(l))}if(!i[e]){const c=o(r,s=>{const n=h(f).getItem(e);n&&s(a.parse(n));{const S=d=>{d.key===e&&s(d.newValue?a.parse(d.newValue):null)};return window.addEventListener("storage",S),()=>window.removeEventListener("storage",S)}}),{subscribe:l,set:g}=c;i[e]={set(s){u(e,s),g(s)},update(s){const n=s(w(c));u(e,n),g(n)},subscribe:l}}return i[e]}const P=m("modeOsPrefers",!1),_=m("modeUserPrefers",void 0),I=m("modeCurrent",!1);function p(){const e=window.matchMedia("(prefers-color-scheme: light)").matches;return P.set(e),e}function O(e){_.set(e)}function k(e){const r=document.documentElement.classList,t="dark";e===!0?r.remove(t):r.add(t),I.set(e)}function x(){const e=document.documentElement.classList,r=localStorage.getItem("modeUserPrefers")==="false",t=!("modeUserPrefers"in localStorage),a=window.matchMedia("(prefers-color-scheme: dark)").matches;r||t&&a?e.add("dark"):e.remove("dark")}export{k as a,O as b,C as c,b as d,v as e,E as f,p as g,I as m,x as s,L as t};
