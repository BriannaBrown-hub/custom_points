const LatestValuesTable = (data) => {
  return (
    <div className="container">
      <p className="text-gray-500 min-w-full text-lg font-bold text-center pb-4">
        Latest Point Values
      </p>
      <div className="bg-white rounded shadow overflow-x-auto">
        <table className="min-w-full bg-white px-4">
          <thead>
            <tr>
              <th className="py-2 px-4 border-b border-gray-200">Device ID</th>
              <th className="py-2 px-4 border-b border-gray-200">Point Type</th>
              <th className="py-2 px-4 border-b border-gray-200">Units</th>
              <th className="py-2 px-4 border-b border-gray-200">Value</th>
              <th className="py-2 px-4 border-b border-gray-200">Time</th>
            </tr>
          </thead>
          <tbody>
            {data.data.map((entry) => (
              <tr key={entry.id}>
                <td className="py-2 px-4 border-b border-gray-200 text-center">
                  {entry.dev_id}
                </td>
                <td className="py-2 px-4 border-b border-gray-200 text-center">
                  {entry.point_type}
                </td>
                <td className="py-2 px-4 border-b border-gray-200 text-center">
                  {entry.units}
                </td>
                <td className="py-2 px-4 border-b border-gray-200 text-center">
                  {entry.value}
                </td>
                <td className="py-2 px-4 border-b border-gray-200 text-center">
                  {entry.time}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default LatestValuesTable;
