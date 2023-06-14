import React, { useState } from "react";

const CustomPointModal = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [formData, setFormData] = useState({
    dev_id: "",
    point_type: "",
    units: "",
    dependent_point_type: "",
    raw_value: null,
    variable_value: "",
    operator: "",
  });

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch(
        "http://localhost:5000/create_custom_point",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(formData),
        }
      );

      if (response.ok) {
        console.log("Custom Point created successfully");
        setIsOpen(false);
      } else {
        console.error("Error creating Custom Point");
      }
    } catch (error) {
      console.error("Error:", error);
    }
  };

  const handleInputChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  return (
    <div>
      <button
        onClick={() => setIsOpen(true)}
        className="bg-blue-500 text-white font-bold py-2 px-4 rounded"
      >
        Create Custom Point
      </button>
      {isOpen && (
        <div className="fixed inset-0 flex items-center justify-center">
          <div className="modal-overlay absolute inset-0 bg-gray-500 opacity-75" />

          <div className="modal-container bg-white w-1/3 rounded shadow-lg z-50">
            <h2 className="text-xl font-bold mb-4">Create Custom Point</h2>
            <form onSubmit={handleSubmit} className="p-4">
              <div className="mb-4">
                <label htmlFor="dev_id" className="block font-bold mb-1">
                  Device ID:
                </label>
                <input
                  type="text"
                  id="dev_id"
                  name="dev_id"
                  value={formData.dev_id}
                  onChange={handleInputChange}
                  className="w-full border border-gray-300 rounded p-2"
                />
              </div>

              <div className="mb-4">
                <label htmlFor="point_type" className="block font-bold mb-1">
                  Point Type:
                </label>
                <input
                  type="text"
                  id="point_type"
                  name="point_type"
                  value={formData.point_type}
                  onChange={handleInputChange}
                  className="w-full border border-gray-300 rounded p-2"
                />
              </div>

              <div className="mb-4">
                <label htmlFor="units" className="block font-bold mb-1">
                  Units:
                </label>
                <input
                  type="text"
                  id="units"
                  name="units"
                  value={formData.units}
                  onChange={handleInputChange}
                  className="w-full border border-gray-300 rounded p-2"
                />
              </div>

              <div className="mb-4">
                <label
                  htmlFor="dependent_point_type"
                  className="block font-bold mb-1"
                >
                  Dependent Point Type:
                </label>
                <input
                  type="text"
                  id="dependent_point_type"
                  name="dependent_point_type"
                  value={formData.dependent_point_type}
                  onChange={handleInputChange}
                  className="w-full border border-gray-300 rounded p-2"
                />
              </div>

              <div className="mb-4">
                <label htmlFor="raw_value" className="block font-bold mb-1">
                  Raw Value:
                </label>
                <input
                  type="text"
                  id="raw_value"
                  name="raw_value"
                  value={formData.raw_value}
                  onChange={handleInputChange}
                  className="w-full border border-gray-300 rounded p-2"
                />
              </div>

              <div className="mb-4">
                <label
                  htmlFor="variable_value"
                  className="block font-bold mb-1"
                >
                  Variable Value:
                </label>
                <input
                  type="text"
                  id="variable_value"
                  name="variable_value"
                  value={formData.variable_value}
                  onChange={handleInputChange}
                  className="w-full border border-gray-300 rounded p-2"
                />
              </div>

              <div className="mb-4">
                <label
                  htmlFor="variable_value"
                  className="block font-bold mb-1"
                >
                  Operator:
                </label>
                <select
                  id="operator"
                  value={formData.operator}
                  onChange={(e) =>
                    setFormData({ ...formData, operator: e.target.value })
                  }
                  className="border border-gray-300 rounded p-2"
                >
                  <option value="+">+</option>
                  <option value="-">-</option>
                  <option value="/">/</option>
                  <option value="*">*</option>
                  <option value="==">==</option>
                  <option value=">=">>=</option>
                  <option value="<=">&lt;=</option>
                  <option value=">">></option>
                  <option value="<">&lt;</option>
                </select>
              </div>

              <button
                type="submit"
                className="bg-blue-500 text-white font-bold py-2 px-4 rounded"
              >
                Submit
              </button>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};

export default CustomPointModal;
