package com.example.models.data;

import java.util.HashMap;
import java.util.Map;

/**
 * DataManager class is a construct for creating DataManager object.
 * <p>
 * Metadata:
 * - metadata: Map object
 * <p>
 * Data:
 * - data: Map object
 * @see MetadataWrapper
 * @see IDataManager
 */
public abstract class DataManager implements IDataManager {

    protected MetadataWrapper metadata;
    protected Map<String, Object> data;

    /**
     * Constructor for DataManager object.
     * @param metadata MetadataWrapper object
     */
    public DataManager(MetadataWrapper metadata) {
        this.metadata = metadata;
        this.data = new HashMap<>();
    }

    /**
     * Metadata Getter for safe access to metadata.
     * @param key String key
     * @return Object value
     */
    @Override
    public Object getMetadataValue(String key) {
        return metadata.metadata().get(key);
    }

    /**
     * Metadata Setter for safe access to metadata.
     * @param key String key
     * @param value Object value
     */
    @Override
    public void updateMetadata(String key, Object value) {
        Map<String, Object> modifiableMetadata = new HashMap<>(metadata.metadata());
        if (value != null) {
            modifiableMetadata.put(key, value);
        } else {
            modifiableMetadata.remove(key);
        }
        this.metadata = new MetadataWrapper(modifiableMetadata);
    }

    /**
     * Data Getter for safe access to data.
     * @param key String key
     * @return Object value
     */
    @Override
    public Object getDataValue(String key) {
        return data.get(key);
    }

    /**
     * Data Setter for safe access to data.
     * @param key String key
     * @param value Object value
     */
    @Override
    public void setDataValue(String key, Object value) {
        data.put(key, value);
    }

    /**
     * Metadata Getter for safe direct access to metadata.
     * @return MetadataWrapper object
     */
    @Override
    public MetadataWrapper getMetadata() {
        return metadata;
    }

    /**
     * Data Getter for safe direct access to data.
     * @return Map object
     */
    @Override
    public Map<String, Object> getData() {
        return data;
    }

    /**
     * Intermediary method to get metadata as a map.
     * @return Map object
     */
    @Override
    public Map<String, Object> getMetadataMap() {
        return metadata.metadata();
    }

    /**
     * Converts DataManager object to map.
     * @return Map object
     */
    public Map<String, Object> toMap() {
        Map<String, Object> result = new HashMap<>();
        result.put("metadata", getMetadataMap());
        result.put("data", getData());
        return result;
    }

    /**
     * Converts DataManager object to string.
     * @return String representation of DataManager object
     */
    @Override
    public String toString() {
        return String.format("%s{Metadata: %s, Data: %s}",
                this.getClass().getSimpleName(),
                metadata != null ? metadata.metadata() : "null",
                data != null ? new HashMap<>(data) : "null");
    }

    /**
     * Compares DataManager object with another object.
     * @param obj Object to compare
     * @return boolean value
     */
    @Override
    public boolean equals(Object obj) {
        if (obj == this) {
            return true;
        }
        if (obj == null || obj.getClass() != this.getClass()) {
            return false;
        }
        DataManager other = (DataManager) obj;
        return metadata.equals(other.metadata) && data.equals(other.data);
    }

    /**
     * Generates hash code for DataManager object.
     * @return int hash code
     */
    @Override
    public int hashCode() {
        return metadata.hashCode() + data.hashCode();
    }
}
