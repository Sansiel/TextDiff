package com.example.user.helloworld;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
      setContentView(R.layout.activity_main);
        Draw2D draw2D = new Draw2D(this);
        setContentView(draw2D);
            }

    private void setContentView(Draw2D draw2D) {
    }

}
