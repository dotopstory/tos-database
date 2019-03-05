!function(e,t){"function"==typeof define&&define.amd?define([],t):"object"==typeof module&&"undefined"!=typeof exports?module.exports=t():e.Papa=t()}(this,function(){"use strict";var e,t,i="undefined"!=typeof self?self:"undefined"!=typeof window?window:void 0!==i?i:{},n=!i.document&&!!i.postMessage,r=n&&/(\?|&)papaworker(=|&|$)/.test(i.location.search),s=!1,a={},o=0,h={parse:function(t,n){var r=(n=n||{}).dynamicTyping||!1;if(C(r)&&(n.dynamicTypingFunction=r,r={}),n.dynamicTyping=r,n.transform=!!C(n.transform)&&n.transform,n.worker&&h.WORKERS_SUPPORTED){var u=function(){if(!h.WORKERS_SUPPORTED)return!1;if(!s&&null===h.SCRIPT_PATH)throw new Error("Script path cannot be determined automatically when Papa Parse is loaded asynchronously. You need to set Papa.SCRIPT_PATH manually.");var t=h.SCRIPT_PATH||e;t+=(-1!==t.indexOf("?")?"&":"?")+"papaworker";var n=new i.Worker(t);return n.onmessage=v,n.id=o++,a[n.id]=n}();return u.userStep=n.step,u.userChunk=n.chunk,u.userComplete=n.complete,u.userError=n.error,n.step=C(n.step),n.chunk=C(n.chunk),n.complete=C(n.complete),n.error=C(n.error),delete n.worker,void u.postMessage({input:t,config:n,workerId:u.id})}var d=null;return t===h.NODE_STREAM_INPUT?(d=new _(n)).getStream():("string"==typeof t?d=n.download?new c(n):new f(n):!0===t.readable&&C(t.read)&&C(t.on)?d=new p(n):(i.File&&t instanceof File||t instanceof Object)&&(d=new l(n)),d.stream(t))},unparse:function(e,t){var i=!1,n=!0,r=",",s="\r\n",a='"';"object"==typeof t&&("string"==typeof t.delimiter&&1===t.delimiter.length&&-1===h.BAD_DELIMITERS.indexOf(t.delimiter)&&(r=t.delimiter),("boolean"==typeof t.quotes||t.quotes instanceof Array)&&(i=t.quotes),"string"==typeof t.newline&&(s=t.newline),"string"==typeof t.quoteChar&&(a=t.quoteChar),"boolean"==typeof t.header&&(n=t.header));var o=new RegExp(a,"g");if("string"==typeof e&&(e=JSON.parse(e)),e instanceof Array){if(!e.length||e[0]instanceof Array)return d(null,e);if("object"==typeof e[0])return d(u(e[0]),e)}else if("object"==typeof e)return"string"==typeof e.data&&(e.data=JSON.parse(e.data)),e.data instanceof Array&&(e.fields||(e.fields=e.meta&&e.meta.fields),e.fields||(e.fields=e.data[0]instanceof Array?e.fields:u(e.data[0])),e.data[0]instanceof Array||"object"==typeof e.data[0]||(e.data=[e.data])),d(e.fields||[],e.data||[]);throw"exception: Unable to serialize unrecognized input";function u(e){if("object"!=typeof e)return[];var t=[];for(var i in e)t.push(i);return t}function d(e,t){var i="";"string"==typeof e&&(e=JSON.parse(e)),"string"==typeof t&&(t=JSON.parse(t));var a=e instanceof Array&&0<e.length,o=!(t[0]instanceof Array);if(a&&n){for(var h=0;h<e.length;h++)0<h&&(i+=r),i+=c(e[h],h);0<t.length&&(i+=s)}for(var u=0;u<t.length;u++){for(var d=a?e.length:t[u].length,l=0;l<d;l++){0<l&&(i+=r);var f=a&&o?e[l]:l;i+=c(t[u][f],l)}u<t.length-1&&(i+=s)}return i}function c(e,t){return null==e?"":e.constructor===Date?JSON.stringify(e).slice(1,25):(e=e.toString().replace(o,a+a),"boolean"==typeof i&&i||i instanceof Array&&i[t]||function(e,t){for(var i=0;i<t.length;i++)if(-1<e.indexOf(t[i]))return!0;return!1}(e,h.BAD_DELIMITERS)||-1<e.indexOf(r)||" "===e.charAt(0)||" "===e.charAt(e.length-1)?a+e+a:e)}}};if(h.RECORD_SEP=String.fromCharCode(30),h.UNIT_SEP=String.fromCharCode(31),h.BYTE_ORDER_MARK="\ufeff",h.BAD_DELIMITERS=["\r","\n",'"',h.BYTE_ORDER_MARK],h.WORKERS_SUPPORTED=!n&&!!i.Worker,h.SCRIPT_PATH=null,h.NODE_STREAM_INPUT=1,h.LocalChunkSize=10485760,h.RemoteChunkSize=5242880,h.DefaultDelimiter=",",h.Parser=m,h.ParserHandle=g,h.NetworkStreamer=c,h.FileStreamer=l,h.StringStreamer=f,h.ReadableStreamStreamer=p,h.DuplexStreamStreamer=_,i.jQuery){var u=i.jQuery;u.fn.parse=function(e){var t=e.config||{},n=[];return this.each(function(e){if("INPUT"!==u(this).prop("tagName").toUpperCase()||"file"!==u(this).attr("type").toLowerCase()||!i.FileReader||!this.files||0===this.files.length)return!0;for(var r=0;r<this.files.length;r++)n.push({file:this.files[r],inputElem:this,instanceConfig:u.extend({},t)})}),r(),this;function r(){if(0!==n.length){var t,i,r,a,o=n[0];if(C(e.before)){var d=e.before(o.file,o.inputElem);if("object"==typeof d){if("abort"===d.action)return t="AbortError",i=o.file,r=o.inputElem,a=d.reason,void(C(e.error)&&e.error({name:t},i,r,a));if("skip"===d.action)return void s();"object"==typeof d.config&&(o.instanceConfig=u.extend(o.instanceConfig,d.config))}else if("skip"===d)return void s()}var c=o.instanceConfig.complete;o.instanceConfig.complete=function(e){C(c)&&c(e,o.file,o.inputElem),s()},h.parse(o.file,o.instanceConfig)}else C(e.complete)&&e.complete()}function s(){n.splice(0,1),r()}}}function d(e){this._handle=null,this._finished=!1,this._completed=!1,this._input=null,this._baseIndex=0,this._partialLine="",this._rowCount=0,this._start=0,this._nextChunk=null,this.isFirstChunk=!0,this._completeResults={data:[],errors:[],meta:{}},function(e){var t=b(e);t.chunkSize=parseInt(t.chunkSize),e.step||e.chunk||(t.chunkSize=null),this._handle=new g(t),(this._handle.streamer=this)._config=t}.call(this,e),this.parseChunk=function(e,t){if(this.isFirstChunk&&C(this._config.beforeFirstChunk)){var n=this._config.beforeFirstChunk(e);void 0!==n&&(e=n)}this.isFirstChunk=!1;var s=this._partialLine+e;this._partialLine="";var a=this._handle.parse(s,this._baseIndex,!this._finished);if(!this._handle.paused()&&!this._handle.aborted()){var o=a.meta.cursor;this._finished||(this._partialLine=s.substring(o-this._baseIndex),this._baseIndex=o),a&&a.data&&(this._rowCount+=a.data.length);var u=this._finished||this._config.preview&&this._rowCount>=this._config.preview;if(r)i.postMessage({results:a,workerId:h.WORKER_ID,finished:u});else if(C(this._config.chunk)&&!t){if(this._config.chunk(a,this._handle),this._handle.paused()||this._handle.aborted())return;a=void 0,this._completeResults=void 0}return this._config.step||this._config.chunk||(this._completeResults.data=this._completeResults.data.concat(a.data),this._completeResults.errors=this._completeResults.errors.concat(a.errors),this._completeResults.meta=a.meta),this._completed||!u||!C(this._config.complete)||a&&a.meta.aborted||(this._config.complete(this._completeResults,this._input),this._completed=!0),u||a&&a.meta.paused||this._nextChunk(),a}},this._sendError=function(e){C(this._config.error)?this._config.error(e):r&&this._config.error&&i.postMessage({workerId:h.WORKER_ID,error:e,finished:!1})}}function c(e){var t;(e=e||{}).chunkSize||(e.chunkSize=h.RemoteChunkSize),d.call(this,e),this._nextChunk=n?function(){this._readChunk(),this._chunkLoaded()}:function(){this._readChunk()},this.stream=function(e){this._input=e,this._nextChunk()},this._readChunk=function(){if(this._finished)this._chunkLoaded();else{if(t=new XMLHttpRequest,this._config.withCredentials&&(t.withCredentials=this._config.withCredentials),n||(t.onload=w(this._chunkLoaded,this),t.onerror=w(this._chunkError,this)),t.open("GET",this._input,!n),this._config.downloadRequestHeaders){var e=this._config.downloadRequestHeaders;for(var i in e)t.setRequestHeader(i,e[i])}if(this._config.chunkSize){var r=this._start+this._config.chunkSize-1;t.setRequestHeader("Range","bytes="+this._start+"-"+r),t.setRequestHeader("If-None-Match","webkit-no-cache")}try{t.send()}catch(e){this._chunkError(e.message)}n&&0===t.status?this._chunkError():this._start+=this._config.chunkSize}},this._chunkLoaded=function(){var e;4===t.readyState&&(t.status<200||400<=t.status?this._chunkError():(this._finished=!this._config.chunkSize||this._start>(null===(e=t.getResponseHeader("Content-Range"))?-1:parseInt(e.substr(e.lastIndexOf("/")+1))),this.parseChunk(t.responseText)))},this._chunkError=function(e){var i=t.statusText||e;this._sendError(new Error(i))}}function l(e){var t,i;(e=e||{}).chunkSize||(e.chunkSize=h.LocalChunkSize),d.call(this,e);var n="undefined"!=typeof FileReader;this.stream=function(e){this._input=e,i=e.slice||e.webkitSlice||e.mozSlice,n?((t=new FileReader).onload=w(this._chunkLoaded,this),t.onerror=w(this._chunkError,this)):t=new FileReaderSync,this._nextChunk()},this._nextChunk=function(){this._finished||this._config.preview&&!(this._rowCount<this._config.preview)||this._readChunk()},this._readChunk=function(){var e=this._input;if(this._config.chunkSize){var r=Math.min(this._start+this._config.chunkSize,this._input.size);e=i.call(e,this._start,r)}var s=t.readAsText(e,this._config.encoding);n||this._chunkLoaded({target:{result:s}})},this._chunkLoaded=function(e){this._start+=this._config.chunkSize,this._finished=!this._config.chunkSize||this._start>=this._input.size,this.parseChunk(e.target.result)},this._chunkError=function(){this._sendError(t.error)}}function f(e){var t;d.call(this,e=e||{}),this.stream=function(e){return t=e,this._nextChunk()},this._nextChunk=function(){if(!this._finished){var e=this._config.chunkSize,i=e?t.substr(0,e):t;return t=e?t.substr(e):"",this._finished=!t,this.parseChunk(i)}}}function p(e){d.call(this,e=e||{});var t=[],i=!0,n=!1;this.pause=function(){d.prototype.pause.apply(this,arguments),this._input.pause()},this.resume=function(){d.prototype.resume.apply(this,arguments),this._input.resume()},this.stream=function(e){this._input=e,this._input.on("data",this._streamData),this._input.on("end",this._streamEnd),this._input.on("error",this._streamError)},this._checkIsFinished=function(){n&&1===t.length&&(this._finished=!0)},this._nextChunk=function(){this._checkIsFinished(),t.length?this.parseChunk(t.shift()):i=!0},this._streamData=w(function(e){try{t.push("string"==typeof e?e:e.toString(this._config.encoding)),i&&(i=!1,this._checkIsFinished(),this.parseChunk(t.shift()))}catch(e){this._streamError(e)}},this),this._streamError=w(function(e){this._streamCleanUp(),this._sendError(e)},this),this._streamEnd=w(function(){this._streamCleanUp(),n=!0,this._streamData("")},this),this._streamCleanUp=w(function(){this._input.removeListener("data",this._streamData),this._input.removeListener("end",this._streamEnd),this._input.removeListener("error",this._streamError)},this)}function _(e){var t=require("stream").Duplex,i=b(e),n=!0,r=!1,s=[],a=null;this._onCsvData=function(e){for(var t=e.data,i=0;i<t.length;i++)a.push(t[i])||this._handle.paused()||this._handle.pause()},this._onCsvComplete=function(){a.push(null)},i.step=w(this._onCsvData,this),i.complete=w(this._onCsvComplete,this),d.call(this,i),this._nextChunk=function(){r&&1===s.length&&(this._finished=!0),s.length?s.shift()():n=!0},this._addToParseQueue=function(e,t){s.push(w(function(){if(this.parseChunk("string"==typeof e?e:e.toString(i.encoding)),C(t))return t()},this)),n&&(n=!1,this._nextChunk())},this._onRead=function(){this._handle.paused()&&this._handle.resume()},this._onWrite=function(e,t,i){this._addToParseQueue(e,i)},this._onWriteComplete=function(){r=!0,this._addToParseQueue("")},this.getStream=function(){return a},(a=new t({readableObjectMode:!0,decodeStrings:!1,read:w(this._onRead,this),write:w(this._onWrite,this)})).once("finish",w(this._onWriteComplete,this))}function g(e){var t,i,n,r=/^\s*-?(\d*\.?\d+|\d+\.?\d*)(e[-+]?\d+)?\s*$/i,s=/(\d{4}-[01]\d-[0-3]\dT[0-2]\d:[0-5]\d:[0-5]\d\.\d+([+-][0-2]\d:[0-5]\d|Z))|(\d{4}-[01]\d-[0-3]\dT[0-2]\d:[0-5]\d:[0-5]\d([+-][0-2]\d:[0-5]\d|Z))|(\d{4}-[01]\d-[0-3]\dT[0-2]\d:[0-5]\d([+-][0-2]\d:[0-5]\d|Z))/,a=this,o=0,u=0,d=!1,c=!1,l=[],f={data:[],errors:[],meta:{}};if(C(e.step)){var p=e.step;e.step=function(t){if(f=t,g())_();else{if(_(),0===f.data.length)return;o+=t.data.length,e.preview&&o>e.preview?i.abort():p(f,a)}}}function _(){if(f&&n&&(y("Delimiter","UndetectableDelimiter","Unable to auto-detect delimiting character; defaulted to '"+h.DefaultDelimiter+"'"),n=!1),e.skipEmptyLines)for(var t=0;t<f.data.length;t++)1===f.data[t].length&&""===f.data[t][0]&&f.data.splice(t--,1);return g()&&function(){if(f){for(var t=0;g()&&t<f.data.length;t++)for(var i=0;i<f.data[t].length;i++){var n=f.data[t][i];e.trimHeaders&&(n=n.trim()),l.push(n)}f.data.splice(0,1)}}(),function(){if(!f||!e.header&&!e.dynamicTyping&&!e.transform)return f;for(var t=0;t<f.data.length;t++){var i,n=e.header?{}:[];for(i=0;i<f.data[t].length;i++){var r=i,s=f.data[t][i];e.header&&(r=i>=l.length?"__parsed_extra":l[i]),e.transform&&(s=e.transform(s,r)),s=v(r,s),"__parsed_extra"===r?(n[r]=n[r]||[],n[r].push(s)):n[r]=s}f.data[t]=n,e.header&&(i>l.length?y("FieldMismatch","TooManyFields","Too many fields: expected "+l.length+" fields but parsed "+i,u+t):i<l.length&&y("FieldMismatch","TooFewFields","Too few fields: expected "+l.length+" fields but parsed "+i,u+t))}return e.header&&f.meta&&(f.meta.fields=l),u+=f.data.length,f}()}function g(){return e.header&&0===l.length}function v(t,i){return n=t,e.dynamicTypingFunction&&void 0===e.dynamicTyping[n]&&(e.dynamicTyping[n]=e.dynamicTypingFunction(n)),!0===(e.dynamicTyping[n]||e.dynamicTyping)?"true"===i||"TRUE"===i||"false"!==i&&"FALSE"!==i&&(r.test(i)?parseFloat(i):s.test(i)?new Date(i):""===i?null:i):i;var n}function y(e,t,i,n){f.errors.push({type:e,code:t,message:i,row:n})}this.parse=function(r,s,a){if(e.newline||(e.newline=function(e){var t=(e=e.substr(0,1048576)).split("\r"),i=e.split("\n"),n=1<i.length&&i[0].length<t[0].length;if(1===t.length||n)return"\n";for(var r=0,s=0;s<t.length;s++)"\n"===t[s][0]&&r++;return r>=t.length/2?"\r\n":"\r"}(r)),n=!1,e.delimiter)C(e.delimiter)&&(e.delimiter=e.delimiter(r),f.meta.delimiter=e.delimiter);else{var o=function(t,i,n,r){for(var s,a,o,u=[",","\t","|",";",h.RECORD_SEP,h.UNIT_SEP],d=0;d<u.length;d++){var c=u[d],l=0,f=0,p=0;o=void 0;for(var _=new m({comments:r,delimiter:c,newline:i,preview:10}).parse(t),g=0;g<_.data.length;g++)if(n&&1===_.data[g].length&&0===_.data[g][0].length)p++;else{var v=_.data[g].length;f+=v,void 0!==o?1<v&&(l+=Math.abs(v-o),o=v):o=v}0<_.data.length&&(f/=_.data.length-p),(void 0===a||l<a)&&1.99<f&&(a=l,s=c)}return{successful:!!(e.delimiter=s),bestDelimiter:s}}(r,e.newline,e.skipEmptyLines,e.comments);o.successful?e.delimiter=o.bestDelimiter:(n=!0,e.delimiter=h.DefaultDelimiter),f.meta.delimiter=e.delimiter}var u=b(e);return e.preview&&e.header&&u.preview++,t=r,i=new m(u),f=i.parse(t,s,a),_(),d?{meta:{paused:!0}}:f||{meta:{paused:!1}}},this.paused=function(){return d},this.pause=function(){d=!0,i.abort(),t=t.substr(i.getCharIndex())},this.resume=function(){d=!1,a.streamer.parseChunk(t,!0)},this.aborted=function(){return c},this.abort=function(){c=!0,i.abort(),f.meta.aborted=!0,C(e.complete)&&e.complete(f),t=""}}function m(e){var t,i=(e=e||{}).delimiter,n=e.newline,r=e.comments,s=e.step,a=e.preview,o=e.fastMode,u=t=void 0===e.quoteChar?'"':e.quoteChar;if(void 0!==e.escapeChar&&(u=e.escapeChar),("string"!=typeof i||-1<h.BAD_DELIMITERS.indexOf(i))&&(i=","),r===i)throw"Comment character same as delimiter";!0===r?r="#":("string"!=typeof r||-1<h.BAD_DELIMITERS.indexOf(r))&&(r=!1),"\n"!==n&&"\r"!==n&&"\r\n"!==n&&(n="\n");var d=0,c=!1;this.parse=function(e,h,l){if("string"!=typeof e)throw"Input must be a string";var f=e.length,p=i.length,_=n.length,g=r.length,m=C(s),v=[],y=[],k=[],b=d=0;if(!e)return M();if(o||!1!==o&&-1===e.indexOf(t)){for(var w=e.split(n),E=0;E<w.length;E++){if(k=w[E],d+=k.length,E!==w.length-1)d+=n.length;else if(l)return M();if(!r||k.substr(0,g)!==r){if(m){if(v=[],I(k.split(i)),N(),c)return M()}else I(k.split(i));if(a&&a<=E)return v=v.slice(0,a),M(!0)}}return M()}for(var S,R=e.indexOf(i,d),x=e.indexOf(n,d),T=new RegExp(u.replace(/[-[\]/{}()*+?.\\^$|]/g,"\\$&")+t,"g");;)if(e[d]!==t)if(r&&0===k.length&&e.substr(d,g)===r){if(-1===x)return M();d=x+_,x=e.indexOf(n,d),R=e.indexOf(i,d)}else if(-1!==R&&(R<x||-1===x))k.push(e.substring(d,R)),d=R+p,R=e.indexOf(i,d);else{if(-1===x)break;if(k.push(e.substring(d,x)),L(x+_),m&&(N(),c))return M();if(a&&v.length>=a)return M(!0)}else for(S=d,d++;;){if(-1===(S=e.indexOf(t,S+1)))return l||y.push({type:"Quotes",code:"MissingQuotes",message:"Quoted field unterminated",row:v.length,index:d}),P();if(S===f-1)return P(e.substring(d,S).replace(T,t));if(t!==u||e[S+1]!==u){if(t===u||0===S||e[S-1]!==u){var O=A(R);if(e[S+1+O]===i){k.push(e.substring(d,S).replace(T,t)),d=S+1+O+p,R=e.indexOf(i,d),x=e.indexOf(n,d);break}var D=A(x);if(e.substr(S+1+D,_)===n){if(k.push(e.substring(d,S).replace(T,t)),L(S+1+D+_),R=e.indexOf(i,d),m&&(N(),c))return M();if(a&&v.length>=a)return M(!0);break}y.push({type:"Quotes",code:"InvalidQuotes",message:"Trailing quote on quoted field is malformed",row:v.length,index:d}),S++}}else S++}return P();function I(e){v.push(e),b=d}function A(t){var i=0;if(-1!==t){var n=e.substring(S+1,t);n&&""===n.trim()&&(i=n.length)}return i}function P(t){return l||(void 0===t&&(t=e.substr(d)),k.push(t),d=f,I(k),m&&N()),M()}function L(t){d=t,I(k),k=[],x=e.indexOf(n,d)}function M(e){return{data:v,errors:y,meta:{delimiter:i,linebreak:n,aborted:c,truncated:!!e,cursor:b+(h||0)}}}function N(){s(M()),v=[],y=[]}},this.abort=function(){c=!0},this.getCharIndex=function(){return d}}function v(e){var t=e.data,i=a[t.workerId],n=!1;if(t.error)i.userError(t.error,t.file);else if(t.results&&t.results.data){var r={abort:function(){n=!0,y(t.workerId,{data:[],errors:[],meta:{aborted:!0}})},pause:k,resume:k};if(C(i.userStep)){for(var s=0;s<t.results.data.length&&(i.userStep({data:[t.results.data[s]],errors:t.results.errors,meta:t.results.meta},r),!n);s++);delete t.results}else C(i.userChunk)&&(i.userChunk(t.results,r,t.file),delete t.results)}t.finished&&!n&&y(t.workerId,t.results)}function y(e,t){var i=a[e];C(i.userComplete)&&i.userComplete(t),i.terminate(),delete a[e]}function k(){throw"Not implemented."}function b(e){if("object"!=typeof e||null===e)return e;var t=e instanceof Array?[]:{};for(var i in e)t[i]=b(e[i]);return t}function w(e,t){return function(){e.apply(t,arguments)}}function C(e){return"function"==typeof e}return r?i.onmessage=function(e){var t=e.data;if(void 0===h.WORKER_ID&&t&&(h.WORKER_ID=t.workerId),"string"==typeof t.input)i.postMessage({workerId:h.WORKER_ID,results:h.parse(t.input,t.config),finished:!0});else if(i.File&&t.input instanceof File||t.input instanceof Object){var n=h.parse(t.input,t.config);n&&i.postMessage({workerId:h.WORKER_ID,results:n,finished:!0})}}:h.WORKERS_SUPPORTED&&(t=document.getElementsByTagName("script"),e=t.length?t[t.length-1].src:"",document.body?document.addEventListener("DOMContentLoaded",function(){s=!0},!0):s=!0),(c.prototype=Object.create(d.prototype)).constructor=c,(l.prototype=Object.create(d.prototype)).constructor=l,(f.prototype=Object.create(f.prototype)).constructor=f,(p.prototype=Object.create(d.prototype)).constructor=p,(_.prototype=Object.create(d.prototype)).constructor=_,h});let origin=location.origin+"/";origin+=origin.indexOf("github.io")>0?"tos-database/":"";const TABLE_NAME="data";self.onmessage=async function(e){let t=e.data,i=t.cmd,n=t.payload;switch(i){case"load":let e=t.dataset,r=n.region,s=n.schema,a=(origin+"assets/data/"+r+"/"+e+".csv").toLowerCase(),o=0,h=new Database(e,r);h.initialize(s).then(()=>{Papa.parse(a,{download:!0,header:!0,skipEmptyLines:!0,step:e=>h.insert(e.data[0],o++),complete:()=>h.transaction.oncomplete=(()=>postResponse(t,n))})})}};class Database{constructor(e,t){this.$database=null,this.$dataset=e,this.$region=t,this.$table=null,this.$transaction=null}initialize(e){return new Promise((t,i)=>{let n=(this.$region+"/"+this.$dataset).toLowerCase(),r=indexedDB.open(n,(new Date).getTime());r.onblocked=i,r.onerror=i,r.onsuccess=(()=>t()),r.onupgradeneeded=(t=>{this.$database=t.target.result,this.$transaction=t.target.transaction,Array.from(this.table.indexNames).forEach(e=>this.table.deleteIndex(e)),e.indexes&&e.indexes.forEach(e=>this.table.createIndex(e,e,{multiEntry:!0})),this.$transaction=null})})}insert(e,t){return new Promise((i,n)=>{for(let t in e)try{!t.startsWith("Description")&&e.hasOwnProperty(t)&&"string"==typeof e[t]&&(e[t].startsWith("[")&&e[t].endsWith("]")?e[t]=JSON.parse(e[t]):e[t].startsWith("{")&&e[t].endsWith("}")?e[t]=JSON.parse(e[t]):e[t]&&!isNaN(e[t])&&(e[t]=+e[t]))}catch(e){}0===t&&this.table.clear();let r=this.table.add(e);r.onblocked=n,r.onerror=n,r.onsuccess=(()=>i())})}get table(){return this.$table=this.$table||this.$database.objectStoreNames.contains(TABLE_NAME)?this.transaction.objectStore(TABLE_NAME):this.$database.createObjectStore(TABLE_NAME,{keyPath:"$ID"})}get transaction(){return this.$transaction=this.$transaction||this.$database.transaction([TABLE_NAME],"readwrite")}}function postResponse(e,t){self.postMessage(Object.assign(e,{payload:t}))}