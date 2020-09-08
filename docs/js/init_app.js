const totalbox = document.getElementById("totalbox");
const mainbox = document.getElementById("mainbox");
const dragdropbox = document.getElementById("dragdropbox");
const divgraph = document.getElementById("divgraph");
const divlog = document.getElementById("divlog");
const logger = document.getElementById('log');
const scroll = document.getElementById('scroll');
const dropArea = totalbox;

Plotly.newPlot('divgraph', [], {title: 'Grafico a plotar'});

(function () {
    if (!console) {
        console = {};
    }
    var old = console.log;
    var counter_indice = 0;
    console.log = function (message) {
        var msg = "";
        counter_indice += 1;

        msg += "<td class='indice'/>" + counter_indice.toString() + "</td>";
        msg += "<td class='texto_log'/>"; 
        if (typeof message == 'object') {
            msg += (JSON && JSON.stringify ? JSON.stringify(message) : String(message));
        } else {
            msg += message;
        }
        msg += "</td>"
        logger.innerHTML += msg;
        scroll.scrollTop = scroll.scrollHeight;
    }
})();



dropArea.addEventListener('dragover', (event) => {
    event.stopPropagation();
    event.preventDefault();
    // Style the drag-and-drop as a "copy file" operation.
    event.dataTransfer.dropEffect = 'copy';

    mainbox.style.opacity = 0.2;
    dragdropbox.style.display = "block";

});

dropArea.addEventListener('drop', (event) => {
    mainbox.style.opacity = 1.0;
    dragdropbox.style.display = "none";

    event.stopPropagation();
    event.preventDefault();

    console.log("Drag and Drop ainda nao foi implementado!");
    // const fileList = event.dataTransfer.files;
    // console.log(fileList);
});


// <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-download" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
//   <path fill-rule="evenodd" d="M.5 8a.5.5 0 0 1 .5.5V12a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V8.5a.5.5 0 0 1 1 0V12a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V8.5A.5.5 0 0 1 .5 8z"/>
//   <path fill-rule="evenodd" d="M5 7.5a.5.5 0 0 1 .707 0L8 9.793 10.293 7.5a.5.5 0 1 1 .707.707l-2.646 2.647a.5.5 0 0 1-.708 0L5 8.207A.5.5 0 0 1 5 7.5z"/>
//   <path fill-rule="evenodd" d="M8 1a.5.5 0 0 1 .5.5v8a.5.5 0 0 1-1 0v-8A.5.5 0 0 1 8 1z"/>
// </svg>