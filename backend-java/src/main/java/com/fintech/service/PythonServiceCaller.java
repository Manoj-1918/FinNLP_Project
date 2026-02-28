package com.fintech.service;

import com.fintech.model.Company;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.util.UriComponentsBuilder;

@Service
public class PythonServiceCaller {

    private final String PYTHON_URL = "http://python-service:5000/sentiment";

    public String callPythonService(Company company) {

        RestTemplate restTemplate = new RestTemplate();

        String url = UriComponentsBuilder
                .fromUriString(PYTHON_URL)
                .queryParam("company", company.getName())
                .queryParam("symbol", company.getSymbol())
                .queryParam("sector", company.getSector())
                .toUriString();

        return restTemplate.getForObject(url, String.class);
    }
}