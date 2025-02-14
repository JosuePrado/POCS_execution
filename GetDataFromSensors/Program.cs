using GetDatafromSensors.src.IIoT.sensorComunication;

/// <summary>
/// Main application entry point.
/// </summary>
class Program
{
    static void Main()
    {
        var config = new ConfigLoader();
        var communicator = new SerialCommunicator(config.PortName, config.BaudRate);

        try
        {
            communicator.OpenConnection();
            string response = communicator.SendCommand("STATUS\r\n");
            Console.WriteLine($"Sensor humidity data: {response}");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
        finally
        {
            communicator.CloseConnection();
        }
    }
}
