$(document).ready(function(){var stream = {mp3: "http://" + g + ":" + h + i + z,},ready=false;$("#jquery_jplayer_1").jPlayer({ready:function(event){ready=true;$(this).jPlayer("setMedia",stream).jPlayer("play");},pause:function(){$(this).jPlayer("clearMedia");},error:function(event){if(ready&&event.jPlayer.error.type===$.jPlayer.error.URL_NOT_SET){$(this).jPlayer("setMedia",stream).jPlayer("play");}},stop:function(event){console.log("stop");$(this).jPlayer("setMedia",stream).jPlayer("play");},swfPath:"js",volume:"0.5",supplied:"mp3",preload:"none",autoPlay:true,wmode:"window",keyEnabled:true,});});var j="extralarge",k="img/nocover.png",a="",b="",c="",d="http://",e="128",f="audio/mpeg",m="TRUE",n="TURE",o="FR",p="TRUE",q="TRUE",r=":",s="TRUE",t="TRUE",u="FALSE",v="FALSE";