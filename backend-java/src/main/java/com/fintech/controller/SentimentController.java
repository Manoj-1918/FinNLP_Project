package com.fintech.controller;

import com.fintech.service.PythonServiceCaller;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api")
@CrossOrigin(origins = "*")
public class SentimentController {

    @Autowired
    private PythonServiceCaller pythonServiceCaller;

    @GetMapping("/sentiment")
    public ResponseEntity<String> analyze(
            @RequestParam String company
    ) {
        String result = pythonServiceCaller.callPythonService(company);
        return ResponseEntity.ok(result);
    }
}
