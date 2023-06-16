// chart1.js
const getOptionChart1Data = (chart1Data) => {
    const xAxisData = chart1Data.map(item => item.fecha_sol);
    const seriesData = chart1Data.map(item => item.count);

    return {
        tooltip: {
            show: true,
            trigger: "axis",
            triggerOn: "mousemove|click"
        },
        dataZoom: {
            show: true,
            start: 50
        },
        xAxis: [
            {
                type: "category",
                data: xAxisData
            }
        ],
        yAxis: [
            {
                type: "value"
            }
        ],
        series: [
            {
                data: seriesData,
                type: "line"
            }
        ]
    };
};
const getOptionChart2Data = (chart2Data) => {
    const data = chart2Data.map(item => ({ name: item.rubro, value: item.count }));

    return {
        tooltip: {
            trigger: "item"
        },
        legend: {
            top: "5%",
            left: "center"
        },
        series: [
            {
                name: "Access From",
                type: "pie",
                radius: ["40%", "70%"],
                avoidLabelOverlap: false,
                itemStyle: {
                    borderRadius: 10,
                    borderColor: "#fff",
                    borderWidth: 2
                },
                label: {
                    show: false,
                    position: "center"
                },
                emphasis: {
                    label: {
                        show: true,
                        fontSize: "40",
                        fontWeight: "bold"
                    }
                },
                labelLine: {
                    show: false
                },
                data: data
            }
        ]
    };
};



// Renderiza el gráfico cuando el documento esté listo
document.addEventListener("DOMContentLoaded", function() {
    // Obtén los datos del contexto para el chart1 y chart2
    const contextData = JSON.parse(document.getElementById("chart1Data").textContent);
    const chart1Data = contextData.solicitudes;
    const chart2Data = contextData.chart2_data;

    // Renderiza el gráfico chart1
    const chart1Container = document.getElementById("chart1");
    const chart1 = echarts.init(chart1Container);
    const chart1Option = getOptionChart1Data(chart1Data);
    chart1.setOption(chart1Option);

    // Renderiza el gráfico chart2
    const chart2Container = document.getElementById("chart2");
    const chart2 = echarts.init(chart2Container);
    const chart2Option = getOptionChart2Data(chart2Data);
    chart2.setOption(chart2Option);
});
