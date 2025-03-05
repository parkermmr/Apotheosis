package com.example.controllers;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.ArgumentMatchers.eq;
import static org.mockito.Mockito.doNothing;
import static org.mockito.Mockito.when;
import org.mockito.MockitoAnnotations;
import org.mockito.junit.jupiter.MockitoExtension;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.test.context.bean.override.mockito.MockitoBean;
import org.springframework.test.web.servlet.MockMvc;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.delete;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.patch;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.put;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

import com.example.models.Template;
import com.example.services.TemplateService;

@WebMvcTest(TemplateController.class)
@ExtendWith(MockitoExtension.class)
@AutoConfigureMockMvc(addFilters = false)
public class TemplateControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @MockitoBean
    private TemplateService templateService;

    @BeforeEach
    public void setUp() {
        MockitoAnnotations.openMocks(this);
    }

    @Test
    public void testCreateTemplate() throws Exception {
        Template template = new Template();
        template.setId("1");
        when(templateService.createTemplate()).thenReturn(template);

        mockMvc.perform(post("/api/v1/template"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.id").value("1"));
    }

    @Test
    public void testGetTemplate() throws Exception {
        Template template = new Template();
        template.setId("1");
        when(templateService.getTemplate("1")).thenReturn(template);

        mockMvc.perform(get("/api/v1/template/1"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.id").value("1"));
    }

    @Test
    public void testUpdateTemplate() throws Exception {
        Template template = new Template();
        template.setId("1");
        when(templateService.updateTemplate(eq("1"), any(Template.class))).thenReturn(template);

        mockMvc.perform(put("/api/v1/template/1")
                .contentType("application/json")
                .content("{}"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.id").value("1"));
    }

    @Test
    public void testPatchTemplate() throws Exception {
        Template template = new Template();
        template.setId("1");
        when(templateService.patchTemplate(eq("1"), any(Template.class))).thenReturn(template);

        mockMvc.perform(patch("/api/v1/template/1")
                .contentType("application/json")
                .content("{}"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.id").value("1"));
    }

    @Test
    public void testDeleteTemplate() throws Exception {
        doNothing().when(templateService).deleteTemplate("1");

        mockMvc.perform(delete("/api/v1/template/1"))
                .andExpect(status().isNoContent());
    }

    @Test
    public void testGetAllTemplates() throws Exception {
        when(templateService.getTemplates()).thenReturn(java.util.List.of(new Template(), new Template()));

        mockMvc.perform(get("/api/v1/template"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.length()").value(2)); // Expect 2 elements
    }
}
