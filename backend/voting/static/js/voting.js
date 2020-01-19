function setCookie(cname, cvalue, exsecs) {
    var d = new Date();
    d.setTime(d.getTime() + (exsecs * 1000));
    var expires = "expires=" + d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

$(document).ready(function () {

    $("#flipCam").click(function () {
        camNo = (camNo+1)%totCam;
        scanner.stop().then(()=>{startCam();});
    })

    $('.modal').modal({
        dismissible: true,
        onCloseEnd: function () {
            scanner.stop();
            console.log('11');
        }
    });
    $("#collapse2").hide();
    $("#manual_show").click(function () {
        $("#collapse2").show();
    });

    $("#qrstart").click(() => {
        startCam();
    });

    $("#btnSubmit").click(function () {
        setCookie("check", "pictoreal", 500);
        for (i in arrPhoto) {
            setCookie("p" + i, arrPhoto[i], 500);
        }
        for (i in arrSketch) {
            setCookie("s" + i, arrSketch[i], 500);
        }
        window.location = "../submit";
    })

    $("#Manual").click(function () {
        let content = $("#idManual").val();
        let chipadd = true;
        if (content[0] == 'p' || content[0] == 'P') {
            if (arrPhoto.length < 3) {
                if (arrPhoto.indexOf(content) > -1) {
                    chipadd = false;
                    alert("You can vote for a particular Photo only once.");
                } else {
                    arrPhoto.push(content);
                    console.log("added " + content);
                    var ps = 'photo';
                    $("#numP").text(arrPhoto.length);
                }
            } else {
                chipadd = false;
                alert("You can vote only for 3 Photo !!");
            }
            console.log(arrPhoto);
        }
        if (content[0] == 's' || content[0] == 'S') {
            if (arrSketch.length < 3) {
                if (arrSketch.indexOf(content) > -1) {
                    chipadd = false;
                    setTimeout(() => alert("You can vote for a particular Sketch only once."), 1);
                } else {
                    arrSketch.push(content);
                    console.log("added " + content);
                    var ps = 'drawing';
                    $("#numS").text(arrSketch.length);
                }
            } else {
                chipadd = false;
                alert("You can vote only for 3 Sketch !!");
            }
            console.log(arrSketch);
        }

        if ((content[0] == 's' || content[0] == 'S' || content[0] == 'p' || content[0] == 'P') && chipadd) {
            $("#chips").append("<div class=\"chip " + ps + "\" data='" + content + "'>\n" +
                "                <div class=\"row\">\n" +
                "\n" +
                "                    <div class=\"row\">\n" +
                "                        <div class=\"input-field col s10 \">\n" +
                "                            <i class=\"material-icons prefix  \">check</i>\n" +
                "                            <input id=\"icon_prefix\" type=\"text\" disabled>\n" +
                "                            <label for=\"icon_prefix\">" + content + "</label>\n" +
                "\n" +
                "                        </div>\n" +
                "                        <div class=\"container\">\n" +
                "                            <i class=\"close material-icons center-align\" onclick=\"voteDelete('" + content + "')\">close</i>\n" +
                "                        </div>\n" +
                "\n" +
                "                    </div>\n" +
                "\n" +
                "\n" +
                "                </div>\n" +
                "\n" +
                "            </div>")
            scanner.stop();
            $(".modal").modal('close')
        }

    })
});


var arrSketch = [];
var arrPhoto = [];

var scanner;
var camNo = -1;
var totCam;

function startCam() {
    scanner = new Instascan.Scanner({
        video: document.getElementById('preview'),
        mirror: false
    })
    Instascan.Camera.getCameras().then(function (cameras) {
        if (camNo === -1) {
            totCam = cameras.length;
            if (cameras.length > 1) {
                camNo = 1;
            } else if (cameras.length > 0) {
                camNo = 0;
            } else {
                console.error('No cameras found.');
            }
        }
        if (camNo !== -1)
            scanner.start(cameras[camNo]);
    }).catch(function (e) {
        console.error(e);
    });

    var lastQr = "";
    scanner.addListener('scan', function (content) {
        if (content != lastQr) {
            lastQr = content;
            let chipadd = true;
            if (content[0] == 'p' || content[0] == 'P') {
                if (arrPhoto.length < 3) {
                    if (arrPhoto.indexOf(content) > -1) {
                        chipadd = false;
                        alert("You can vote for a particular Photo only once.");
                    } else {
                        arrPhoto.push(content);
                        console.log("added " + content);
                        var ps = 'photo';
                        $("#numP").text(arrPhoto.length);
                    }
                } else {
                    chipadd = false;
                    alert("You can vote only for 3 Photo !!");
                }
                console.log(arrPhoto);
            }
            if (content[0] == 's' || content[0] == 'S') {
                if (arrSketch.length < 3) {
                    if (arrSketch.indexOf(content) > -1) {
                        chipadd = false;
                        setTimeout(() => alert("You can vote for a particular Sketch only once."), 1);
                    } else {
                        arrSketch.push(content);
                        console.log("added " + content);
                        var ps = 'drawing';
                        $("#numS").text(arrSketch.length);
                    }
                } else {
                    chipadd = false;
                    alert("You can vote only for 3 Sketch !!");
                }
                console.log(arrSketch);
            }

            if ((content[0] == 's' || content[0] == 'S' || content[0] == 'p' || content[0] == 'P') && chipadd) {
                $("#chips").append("<div class=\"chip " + ps + "\" data='" + content + "'>\n" +
                    "                <div class=\"row\">\n" +
                    "\n" +
                    "                    <div class=\"row\">\n" +
                    "                        <div class=\"input-field col s10 \">\n" +
                    "                            <i class=\"material-icons prefix  \">check</i>\n" +
                    "                            <input id=\"icon_prefix\" type=\"text\" disabled>\n" +
                    "                            <label for=\"icon_prefix\">" + content + "</label>\n" +
                    "\n" +
                    "                        </div>\n" +
                    "                        <div class=\"container\">\n" +
                    "                            <i class=\"close material-icons center-align\" onclick=\"voteDelete('" + content + "')\">close</i>\n" +
                    "                        </div>\n" +
                    "\n" +
                    "                    </div>\n" +
                    "\n" +
                    "\n" +
                    "                </div>\n" +
                    "\n" +
                    "            </div>")
                scanner.stop();
                $(".modal").modal('close')

            }
        }
    });

}


function voteDelete(x) {

    if (x[0] === 'P') {
        var index = arrPhoto.indexOf(x);
        if (index > -1) {
            arrPhoto.splice(index, 1);
        }
        console.log(arrPhoto);
        $("#numP").text(arrPhoto.length);
    } else {
        var index = arrSketch.indexOf(x);
        if (index > -1) {
            arrSketch.splice(index, 1);
        }
        console.log(arrSketch);
        $("#numS").text(arrSketch.length);
    }
}