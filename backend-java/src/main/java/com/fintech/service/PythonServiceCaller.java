package com.fintech.service;

import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class PythonServiceCaller {

    private final RestTemplate restTemplate = new RestTemplate();

    public String callPythonService(String company) {
        String pythonUrl = "http://127.0.0.1:5000/sentiment?company=" + company;
        return restTemplate.getForObject(pythonUrl, String.class);
    }
}
