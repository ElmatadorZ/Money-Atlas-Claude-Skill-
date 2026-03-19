class InsightEngine:

    def generate(self, smc_layers):

        insights = []

        for layer in smc_layers:

            if layer.state == "accumulating":
                insights.append(
                    f"Layer {layer.layer}: มีสัญญาณสะสมของทุนใหญ่"
                )

            elif layer.state == "distributing":
                insights.append(
                    f"Layer {layer.layer}: มีแรงขายจากผู้ถือครอง"
                )

        return insights
