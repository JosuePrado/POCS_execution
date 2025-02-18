using GetDatafromSensors.src.IIoT.sensorComunication;

/// <summary>
/// Main application entry point.
/// </summary>
class Program
{
    static void Main()
    {
        var config = new ConfigLoader();
        var communicator = new SerialCommunicator(config.PortName, config.BaudRate,
                                                    config.Parity, config.DataBits, config.StopBits);

        try
        {
            communicator.OpenConnection();

            byte[] commands = [0x16, 0x16, 0x01, 0x01, 0xFF, 0x40, 0x02, 0x49, 0x03, 0x94, 0xC6];
            string response = communicator.SendCommand(commands);

            Console.WriteLine($"Status: {response}");
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
