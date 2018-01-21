Chart.defaults.global.responsive = false;

var chartData = {
  labels : [{% for item in labels %}
             "{{item}}",
            {% endfor %}],
  datasets : [{
      label: '{{ legend }}',
      fill: true,
      lineTension: 0.1,
      backgroundColor: "rgba(75,192,192,0.4)",
      borderColor: "rgba(75,192,192,1)",
      borderCapStyle: 'butt',
      borderDash: [],
      borderDashOffset: 0.0,
      borderJoinStyle: 'miter',
      pointBorderColor: "rgba(75,192,192,1)",
      pointBackgroundColor: "#fff",
      pointBorderWidth: 1,
      pointHoverRadius: 5,
      pointHoverBackgroundColor: "rgba(75,192,192,1)",
      pointHoverBorderColor: "rgba(220,220,220,1)",
      pointHoverBorderWidth: 2,
      pointRadius: 1,
      pointHitRadius: 10,
      data : [{% for item in values %}
                {{item}},
              {% endfor %}],
      spanGaps: false
  }]
}

var ctx = document.getElementById("myChart").getContext("2d");

var myChart = new Chart(ctx, {
  type: 'bar',
  data: chartData,
  options: {
         legend: {
            display: false
         },
         tooltips: {
            enabled: false
         }
    }
});