package com.example.services;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertNull;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import com.example.models.Template;

public class TemplateServiceTest {

    private TemplateService templateService;

    @BeforeEach
    public void setUp() {
        templateService = new TemplateService();
    }

    @Test
    public void testCreateTemplate() {
        Template template = templateService.createTemplate();
        assertNotNull(template);
        assertNotNull(template.getId());
        assertEquals(template, templateService.getTemplate(template.getId()));
    }

    @Test
    public void testGetTemplate() {
        Template template = templateService.createTemplate();
        String id = template.getId();

        Template retrieved = templateService.getTemplate(id);
        assertNotNull(retrieved);
        assertEquals(id, retrieved.getId());
    }

    @Test
    public void testUpdateTemplate() {
        Template template = templateService.createTemplate();
        String id = template.getId();

        Template updatedTemplate = new Template();
        updatedTemplate.setId(id);
        Template result = templateService.updateTemplate(id, updatedTemplate);
        assertNotNull(result);
        assertEquals(id, result.getId());
    }

    @Test
    public void testPatchTemplate() {
        Template template = templateService.createTemplate();
        String id = template.getId();

        Template patchTemplate = new Template();
        patchTemplate.setId("patched-id");

        Template result = templateService.patchTemplate(id, patchTemplate);
        assertNotNull(result);
        assertEquals("patched-id", result.getId());
    }

    @Test
    public void testDeleteTemplate() {
        Template template = templateService.createTemplate();
        String id = template.getId();

        templateService.deleteTemplate(id);
        assertNull(templateService.getTemplate(id));
    }

    @Test
    public void testGetAllTemplates() {
        assertEquals(0, templateService.getTemplates().size());

        templateService.createTemplate();
        templateService.createTemplate();

        assertEquals(2, templateService.getTemplates().size());
    }
}
