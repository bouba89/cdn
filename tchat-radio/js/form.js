    var geoSuccess = function (position) { // Ceci s'exécutera si l'utilisateur accepte la géolocalisation
        startPos = position;
        userlat = startPos.coords.latitude;
        userlon = startPos.coords.longitude;
        $.ajax({
            url: "https://nominatim.openstreetmap.org/reverse", // URL de Nominatim
            type: 'get', // Requête de tyopenstreetmappe GET
            data: "format=json&lat="+userlat+"&lon="+userlon+"&zoom=18&addressdetails=1" // Données envoyées (q -> adresse complète, format -> format attendu pour la réponse, limit -> nombre de réponses attendu, polygon_svg -> fournit les données de polygone de la réponse en svg)
        }).done(function (reponse) {
             if (reponse != "") {
                if(reponse['address']['village']){
                       $("#city").val(reponse['address']['village']);
                }else{
                      $("#city").val(reponse['address']['town']);
                 }
            }
        }).fail(function (error) {
            alert(error);
        });
    };
    var geoFail = function () { // Ceci s'exécutera si l'utilisateur refuse la géolocalisation
        console.log("refus");
    };
    // La ligne ci-dessous cherche la position de l'utilisateur et déclenchera la demande d'accord
    navigator.geolocation.getCurrentPosition(geoSuccess, geoFail);