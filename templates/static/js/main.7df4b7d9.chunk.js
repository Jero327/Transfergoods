(this.webpackJsonpreact_transfergoods=this.webpackJsonpreact_transfergoods||[]).push([[0],{26:function(e,t,n){e.exports=n(44)},31:function(e,t,n){},44:function(e,t,n){"use strict";n.r(t);var a=n(1),r=n.n(a),c=n(13),o=n.n(c),l=(n(31),n(8)),i=n(9),s=n(11),u=n(10),p=function(e){Object(s.a)(n,e);var t=Object(u.a)(n);function n(){return Object(l.a)(this,n),t.apply(this,arguments)}return Object(i.a)(n,[{key:"render",value:function(){return r.a.createElement("div",{className:"text-center"},r.a.createElement("h1",null,"Transfergoods-Citys"))}}]),n}(a.Component),m=n(66),h=n(67),f=n(68),g=n(65),y=n(70),d=n(62),E=n(63),v=n(69),b=n(22),j=n(57),C=n(58),O=n(59),k=n(60),S=n(61),w="http://127.0.0.1:8000/api/citys/",T=function(e){Object(s.a)(n,e);var t=Object(u.a)(n);function n(){var e;Object(l.a)(this,n);for(var a=arguments.length,r=new Array(a),c=0;c<a;c++)r[c]=arguments[c];return(e=t.call.apply(t,[this].concat(r))).state={pk:0,name:""},e.onChange=function(t){e.setState(Object(b.a)({},t.target.name,t.target.value))},e.createCity=function(t){t.preventDefault();var n={method:"POST",headers:{Accept:"application/json","Content-Type":"application/json;charset=UTF-8"},body:JSON.stringify(e.state)};fetch(w,n).then((function(){e.props.resetState(),e.props.toggle()}))},e.editCity=function(t){t.preventDefault();var n={method:"PUT",headers:{Accept:"application/json","Content-Type":"application/json;charset=UTF-8"},body:JSON.stringify(e.state)};fetch(w+e.state.pk,n).then((function(){e.props.resetState(),e.props.toggle()}))},e.defaultIfEmpty=function(e){return""===e?"":e},e}return Object(i.a)(n,[{key:"componentDidMount",value:function(){if(this.props.city){var e=this.props.city,t=e.pk,n=e.name;this.setState({pk:t,name:n})}}},{key:"render",value:function(){return r.a.createElement(j.a,{onSubmit:this.props.city?this.editCity:this.createCity},r.a.createElement(C.a,null,r.a.createElement(O.a,{for:"name"},"Name:"),r.a.createElement(k.a,{type:"text",name:"name",onChange:this.onChange,value:this.defaultIfEmpty(this.state.name)})),r.a.createElement(S.a,null,"Save"))}}]),n}(r.a.Component),A=function(e){Object(s.a)(n,e);var t=Object(u.a)(n);function n(){var e;Object(l.a)(this,n);for(var a=arguments.length,r=new Array(a),c=0;c<a;c++)r[c]=arguments[c];return(e=t.call.apply(t,[this].concat(r))).state={modal:!1},e.toggle=function(){e.setState((function(e){return{modal:!e.modal}}))},e}return Object(i.a)(n,[{key:"render",value:function(){var e=this.props.create,t="Edit City",n=r.a.createElement(v.a,{onClick:this.toggle},"Edit");return e&&(t="Create New City",n=r.a.createElement(v.a,{color:"primary",className:"float-right",onClick:this.toggle,style:{minWidth:"100px"},variant:"contained"},"Create New")),r.a.createElement(a.Fragment,null,n,r.a.createElement(y.a,{isOpen:this.state.modal,toggle:this.toggle},r.a.createElement(d.a,{toggle:this.toggle},t),r.a.createElement(E.a,null,r.a.createElement(T,{resetState:this.props.resetState,toggle:this.toggle,city:this.props.city}))))}}]),n}(a.Component),N=n(64),F=function(e){Object(s.a)(n,e);var t=Object(u.a)(n);function n(){var e;Object(l.a)(this,n);for(var a=arguments.length,r=new Array(a),c=0;c<a;c++)r[c]=arguments[c];return(e=t.call.apply(t,[this].concat(r))).state={modal:!1},e.toggle=function(){e.setState((function(e){return{modal:!e.modal}}))},e.deleteCity=function(t){fetch(w+t,{method:"DELETE",headers:{Accept:"application/json","Content-Type":"application/json;charset=UTF-8"}}).then((function(){e.props.resetState(),e.toggle()}))},e}return Object(i.a)(n,[{key:"render",value:function(){var e=this;return r.a.createElement(a.Fragment,null,r.a.createElement(v.a,{color:"danger",onClick:function(){return e.toggle()}},"Delete"),r.a.createElement(y.a,{isOpen:this.state.modal,toggle:this.toggle},r.a.createElement(d.a,{toggle:this.toggle},"Confirm delete?"),r.a.createElement(N.a,null,r.a.createElement(v.a,{type:"button",onClick:function(){return e.toggle()}},"Cancel"),r.a.createElement(v.a,{type:"button",color:"primary",onClick:function(){return e.deleteCity(e.props.pk)}},"Yes"))))}}]),n}(a.Component),D=function(e){Object(s.a)(n,e);var t=Object(u.a)(n);function n(){return Object(l.a)(this,n),t.apply(this,arguments)}return Object(i.a)(n,[{key:"render",value:function(){var e=this,t=this.props.citys;return r.a.createElement(g.a,{dark:!0},r.a.createElement("thead",null,r.a.createElement("tr",null,r.a.createElement("th",null,"Name"),r.a.createElement("th",null))),r.a.createElement("tbody",null,!t||t.length<=0?r.a.createElement("tr",null,r.a.createElement("td",{colSpan:"6",align:"center"},r.a.createElement("b",null,"Let's add some citys"))):t.map((function(t){return r.a.createElement("tr",{key:t.pk},r.a.createElement("td",null,t.name),r.a.createElement("td",{align:"center"},r.a.createElement(A,{create:!1,city:t,resetState:e.props.resetState}),"\xa0\xa0",r.a.createElement(F,{pk:t.pk,resetState:e.props.resetState})))}))))}}]),n}(a.Component),x=function(e){Object(s.a)(n,e);var t=Object(u.a)(n);function n(){var e;Object(l.a)(this,n);for(var a=arguments.length,r=new Array(a),c=0;c<a;c++)r[c]=arguments[c];return(e=t.call.apply(t,[this].concat(r))).state={citys:[]},e.getCitys=function(){fetch(w,{method:"GET",headers:{Accept:"application/json","Content-Type":"application/json;charset=UTF-8"}}).then((function(e){return e.json()})).then((function(t){return e.setState({citys:t})}))},e.resetState=function(){e.getCitys()},e}return Object(i.a)(n,[{key:"componentDidMount",value:function(){this.resetState()}},{key:"render",value:function(){return r.a.createElement(m.a,{style:{marginTop:"20px"}},r.a.createElement(h.a,null,r.a.createElement(f.a,null,r.a.createElement(D,{citys:this.state.citys,resetState:this.resetState}))),r.a.createElement(h.a,null,r.a.createElement(f.a,null,r.a.createElement(A,{create:!0,resetState:this.resetState}))))}}]),n}(a.Component),U=function(e){Object(s.a)(n,e);var t=Object(u.a)(n);function n(){return Object(l.a)(this,n),t.apply(this,arguments)}return Object(i.a)(n,[{key:"render",value:function(){return r.a.createElement(a.Fragment,null,r.a.createElement(p,null),r.a.createElement(x,null))}}]),n}(a.Component);Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));n(43);o.a.render(r.a.createElement(r.a.StrictMode,null,r.a.createElement(U,null)),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()})).catch((function(e){console.error(e.message)}))}},[[26,1,2]]]);
//# sourceMappingURL=main.7df4b7d9.chunk.js.map