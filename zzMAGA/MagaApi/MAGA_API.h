#pragma once
#ifdef ATLAS
	#include "API\Atlas\Atlas.h"
#else
	#include "API\ARK\Ark.h"
#endif
#ifdef MAGA_EXPORTS
	#define MAGA_API __declspec(dllexport)
#else
	#define MAGA_API __declspec(dllimport)
	#pragma comment(lib, "zzMAGA.lib")
#endif

namespace MAGA::ORP
{
	/* Returns true if location is inside <teamid> ORP location */
	MAGA_API bool isPositionInsideOrpLocation(const int& teamid, const FVector& location);
}

namespace MAGA::PvpCooldown
{
	/*Gets players cooldown by <steamid>, value returned in Seconds */
	MAGA_API uint64 getPlayerCooldownSeconds(const long long& steamid, AShooterPlayerController* player);

	/*Gets players cooldown by <AController>, value returned in Seconds */
	inline MAGA_API uint64 getPlayerCooldownSeconds(AController* player);

	/*Gets players cooldown by <AShooterPlayerController>, value returned in Seconds */
	inline MAGA_API uint64 getPlayerCooldownSeconds(AShooterPlayerController* player);

	/*Gets players cooldown by <AShooterCharacter>, value returned in Seconds */
	inline MAGA_API uint64 getPlayerCooldownSeconds(AShooterCharacter* player_character);
	


	/* Sets cooldown on player by SteamID, raidcooldown default = false */
	MAGA_API void setPlayerCooldDownSeconds(const long long& steamid, bool raid = false);

	/* Sets cooldown on player by <AController>, raidcooldown default = false */
	MAGA_API void setPlayerCooldDownSeconds(AController* player, bool raid = false);

	/* Sets cooldown on player by <AShooterPlayerController>, raidcooldown default = false */
	MAGA_API void setPlayerCooldDownSeconds(AShooterPlayerController* player, bool raid = false);

	/* Sets cooldown on player by <AShooterCharacter>, raidcooldown default = false */
	MAGA_API void setPlayerCooldDownSeconds(AShooterCharacter* player_character, bool raid = false);

}