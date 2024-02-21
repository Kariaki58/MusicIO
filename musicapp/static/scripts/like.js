let formData = new FormData()
let localData = JSON.parse(localStorage.getItem('current_user'))


let userId = localData['id']

formData.append('user', userId)

function Plot2d(xValues, yValues, maxdata) {
  new Chart("plot2d", {
    type: "line",
    data: {
        labels: xValues,
        datasets: [{
            fill: false,
            backgroundColor: "rgba(0,0,255,1.0)",
            data: yValues,
            borderColor: 'red',
            pointStyle: 'circle',
            pointRadius: 7
        }]
    },
    options: {
        legend: {display: false},
        scales: {
            yAxes: [{
                ticks: {
                    min: 0,
                    max: maxdata + 3,
                    fontColor: '#ffffff',
                    fontSize: 16
                },
                gridLines: { color: "#131c2b" }
            }],
            xAxes: [{
                ticks: {
                    fontColor: '#ffffff',
                    fontSize: 16
                },
                gridLines: { color: "#131c2b" }
            }],
          },
      }
  });
}

fetch('http://127.0.0.1:5000/likes', {
    method: 'POST',
    body: formData
})
.then(res => res.json())
.then(data => {
    Plot2d(data['X_value'], data['Y_value'], Math.max(...data['Y_value']))
})
.catch(err => console.error(err))