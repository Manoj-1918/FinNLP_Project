package com.fintech.controller;

import com.fintech.model.Company;
import com.fintech.service.CompanyService;
import com.fintech.service.PythonServiceCaller;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api")
@CrossOrigin(origins = "*")
public class SentimentController {

    @Autowired
    private CompanyService companyService;

    @Autowired
    private PythonServiceCaller pythonServiceCaller;

    @GetMapping("/sentiment")
    public ResponseEntity<?> analyze(@RequestParam String symbol) {

        Company company = companyService.getCompany(symbol);

        if (company == null) {
            return ResponseEntity.badRequest().body("Company not found");
        }

        String result = pythonServiceCaller.callPythonService(company);
        return ResponseEntity.ok(result);
    }
}