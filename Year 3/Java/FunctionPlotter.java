package A_01;

import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.chart.XYChart;
import javafx.scene.control.*;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;
import javafx.scene.chart.LineChart;
import javafx.scene.chart.NumberAxis;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;

/**
 * Graph GUI for plotting functions
 * @author Eimear Foley
 * @version 1 (30th Novemeber 2017)
 */
public class FunctionPlotter extends Application {

    /**
     *
     * @param primaryStage state
     * @throws Exception ..
     */
    @Override
    public void start(Stage primaryStage) throws Exception{
        //set title of of stage
        primaryStage.setTitle("Function Plotter");

        //specify components of the graph for the function
        NumberAxis xAxis = new NumberAxis();
        xAxis.setLabel("x-axis");
        NumberAxis yAxis = new NumberAxis();
        yAxis.setLabel("y-axis");
        LineChart linechart = new LineChart(xAxis, yAxis);
        GridPane grid = new GridPane();
        grid.add(linechart, 0,0, 5,1);

        //Defining components of interactive part of GUI for the function plotter
        ToggleGroup group = new ToggleGroup();
        Label pickSolver = new Label("Choose a solver: ");
        RadioButton falsePos = new RadioButton();
        falsePos.setText("False Position Solver");
        falsePos.setToggleGroup(group);
        RadioButton secant = new RadioButton();
        secant.setText("Secant Solver");
        secant.setToggleGroup(group);
        Label minLabel = new Label("Enter lower bound: ");
        Label maxLabel = new Label("Enter upper bound: ");
        TextField max_num = new TextField();
        TextField min_num = new TextField();
        Button calculate = new Button("Calculate");

        //Handle 'calculate' event
        calculate.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent event) {
                double max = Double.parseDouble(max_num.getText());
                double min = Double.parseDouble(min_num.getText());
                double y = 0.0;
                XYChart.Series<Number, Number> series = new XYChart.Series<Number, Number>();
                series.setName(" f(x) = x - 2.5 * sin(x) * sin(x) ");
                linechart.getData().clear();
                //
                RadioButton chosenSolver = (RadioButton) group.getSelectedToggle();
                for (double x = min; x <= max; x += 0.25){
                    //Check which solver the user chose
                    if (chosenSolver == falsePos){
                        y = FalsePositionSolver.f(x);
                    }
                    else {
                        y = SecantSolver.f(x);
                    }
                    //Add data to XYChart series
                    series.getData().add(new XYChart.Data<>(x, y));
                }
                //Add data from XYChart series to linechart
                linechart.getData().add(series);
                grid.add(linechart, 0,0, 5,1);
            }
        });

        //Add interactive components to GUI
        grid.add(pickSolver, 2, 1);
        grid.setMargin(pickSolver, new Insets(10,5,5,30));
        grid.add(falsePos, 3, 1);
        grid.add(secant, 4,1);
        grid.add(minLabel, 2, 2);
        grid.setMargin(minLabel, new Insets(10,5,5,30));
        grid.add(min_num, 3, 2);
        grid.add(maxLabel, 2,3);
        grid.setMargin(maxLabel, new Insets(10,5,5,30));
        grid.add(max_num, 3,3);
        grid.add(calculate, 3, 5);
        grid.setMargin(calculate, new Insets(10,5,5,0));

        //Creating a scene object
        Scene scene = new Scene(grid, 600, 600);
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args){
        launch(args);
    }
}
